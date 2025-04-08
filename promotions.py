from abc import ABC, abstractmethod


class Promotion(ABC):
    """Abstract base class for all promotions.
    Each promotion must define its own apply_promotion logic.
    """
    
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        """
        Apply the promotion logic to a product for a given quantity.

        :param product: The product being purchased
        :param quantity: The amount of the product being purchased
        :return: The final price after applying the promotion
        """
        pass


class PercentDiscount(Promotion):
    """Promotion that gives a percentage discount on the total price."""
    
    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity):
        """
        Apply a percentage discount to the total price.

        :param product: The product being purchased
        :param quantity: The amount of the product being purchased
        :return: Discounted total price
        """
        discount = product.price * (self.percent / 100)
        return (product.price - discount) * quantity


class SecondHalfPrice(Promotion):
    """Promotion where every second item is sold at half price."""
    
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        """
        Apply a half-price discount to every second item.

        :param product: The product being purchased
        :param quantity: The amount of the product being purchased
        :return: Discounted total price
        """
        full_price_items = quantity // 2 + quantity % 2
        half_price_items = quantity // 2
        return (full_price_items * product.price) + (half_price_items * product.price * 0.5)


class ThirdOneFree(Promotion):
    """Promotion where every third item is free (3 for 2 deal)."""
    
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        """
        Apply a '3 for 2' discount—every third item is free.

        :param product: The product being purchased
        :param quantity: The amount of the product being purchased
        :return: Discounted total price
        """
        chargeable_items = quantity - (quantity // 3)
        return chargeable_items * product.price
