"""
Unit tests for all product types and promotions in the Best Buy 2 project.
Includes tests for core product functionality, special product types, and promotion logic.
"""
import pytest
from products import Product, NonStockedProduct, LimitedProduct
from promotions import PercentDiscount, SecondHalfPrice, ThirdOneFree

def test_creating_product():
    """
    Test that a Product can be created with valid parameters.
    """
    product = Product("MacBook", price=1450, quantity=100)
    assert product.name == "MacBook"
    assert product.price == 1450
    assert product.quantity == 100
    assert product.active


def test_creating_product_data():
    """
    Test that creating a product with invalid input
    (empty name or negative price) raises an Exception.
    """
    # Empty name should raise an exception
    with pytest.raises(Exception):
        Product("", price=1450, quantity=100)

    # Negative price should raise an exception
    with pytest.raises(Exception):
        Product("MacBook Air", price=-100, quantity=50)


def test_product_becomes_inactive_when_out_of_stock():
    """
    Test that when the product is bought to zero quantity,
    it becomes inactive.
    """
    product = Product("test_product", price=25, quantity=1)
    product.buy(1)

    assert not product.active


def test_buy_reduces_quantity_and_returns_total_price():
    """
    Test that buying a product reduces its quantity
    and returns the correct total price.
    """
    product = Product("test_product", price=100, quantity=10)
    total_price = product.buy(3)

    assert total_price == 300
    assert product.quantity == 7


def test_buying_more_than_available_raises_exception():
    """
    Test that trying to buy more quantity than is available
    raises an Exception.
    """
    product = Product("test_product", price=50, quantity=5)

    with pytest.raises(Exception):
        product.buy(10)


# Tests für NonStockedProduct
def test_creating_non_stocked_product():
    """
    Test that a NonStockedProduct can be created with valid parameters.
    """
    product = NonStockedProduct("Windows License", price=200)
    assert product.name == "Windows License"
    assert product.price == 200
    assert product.quantity == 0
    assert product.active  # NonStockedProduct sollte immer aktiv sein


def test_non_stocked_product_always_active():
    """
    Test that a NonStockedProduct remains active even when quantity is 0.
    """
    product = NonStockedProduct("Windows License", price=200)
    assert product.active  # Initial aktiv
    
    # Versuche, die Menge zu ändern (sollte keine Auswirkung haben)
    product.set_quantity(10)
    assert product.quantity == 0  # Menge sollte immer 0 bleiben
    assert product.active  # Sollte immer noch aktiv sein


def test_non_stocked_product_can_be_bought():
    """
    Test that a NonStockedProduct can be bought even when quantity is 0.
    """
    product = NonStockedProduct("Windows License", price=200)
    total_price = product.buy(5)  # Kauft 5 Lizenzen
    
    assert total_price == 1000  # 5 * 200
    assert product.quantity == 0  # Menge sollte immer 0 bleiben
    assert product.active  # Sollte immer noch aktiv sein


# Tests für LimitedProduct
def test_creating_limited_product():
    """
    Test that a LimitedProduct can be created with valid parameters.
    """
    product = LimitedProduct("Shipping", price=10, quantity=5, maximum=1)
    assert product.name == "Shipping"
    assert product.price == 10
    assert product.quantity == 5
    assert product.maximum == 1
    assert product.active


def test_limited_product_respects_maximum():
    """
    Test that a LimitedProduct cannot be bought in quantities exceeding the maximum.
    """
    product = LimitedProduct("Shipping", price=10, quantity=5, maximum=1)
    
    # Kaufen innerhalb des Limits sollte funktionieren
    total_price = product.buy(1)
    assert total_price == 10
    assert product.quantity == 4
    
    # Kaufen über dem Limit sollte eine Exception auslösen
    with pytest.raises(Exception):
        product.buy(2)


def test_limited_product_becomes_inactive_when_out_of_stock():
    """
    Test that a LimitedProduct becomes inactive when out of stock.
    """
    product = LimitedProduct("Shipping", price=10, quantity=1, maximum=1)
    product.buy(1)
    
    assert product.quantity == 0
    assert not product.active  # Sollte inaktiv sein, wenn Menge 0 ist


def test_limited_product_show_method():
    """
    Test that the show method of LimitedProduct includes the maximum information.
    """
    product = LimitedProduct("Shipping", price=10, quantity=5, maximum=1)
    show_output = product.show()
    
    assert "Shipping" in show_output
    assert "Price: 10" in show_output
    assert "Quantity: 5" in show_output
    assert "Max per order: 1" in show_output
    assert "Active: True" in show_output


def test_second_half_price_promotion():
    """
    Test that the SecondHalfPrice promotion applies 50% discount to every second item.
    Buying 2 should result in price for 1.5 items.
    """
    product = Product("MacBook Air M2", price=1000, quantity=10)
    promotion = SecondHalfPrice("Second Half price!")
    product.set_promotion(promotion)

    total = product.buy(2)
    assert total == 1500  # 1 full + 1 half = 1000 + 500


def test_third_one_free_promotion():
    """
    Test that the ThirdOneFree promotion gives every third item for free.
    Buying 3 should result in price for 2 items.
    """
    product = Product("Bose Earbuds", price=300, quantity=10)
    promotion = ThirdOneFree("Third One Free!")
    product.set_promotion(promotion)

    total = product.buy(3)
    assert total == 600  # 2 paid, 1 free


def test_percent_discount_promotion():
    """
    Test that the PercentDiscount promotion correctly reduces the total price by the given percentage.
    """
    product = NonStockedProduct("Windows License", price=200)
    promotion = PercentDiscount("30% off!", percent=30)
    product.set_promotion(promotion)

    total = product.buy(1)
    assert total == 140.0  # 200 - 30% = 140
