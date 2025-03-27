import pytest
from products import Product

def test_creating_product():
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
