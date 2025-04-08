class Product:
    """This class represents a product with name, price, quantity, and active status."""

    def __init__(self, name, price=0.0, quantity=0): #Constructor
        """Create a new product and check if the values are valid"""

        # check for string and not empty
        if not isinstance(name, str) or not name.strip():
            raise Exception("Name must be a non-empty string.")

        # check for int or float and greater than 0
        if not isinstance(price, (int, float)) or price <= 0:
            raise Exception("Price must be greater than 0.")

        #check for int and greater than 0
        if not isinstance(quantity, int) or quantity < 0:
            raise Exception("Quantity must be a non-negative integer.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def buy(self, amount: int) -> float:
        """
        Buy a number of items. Update stock and return total price.

        :param amount: number of items to buy
        :return: total price
        """
        if not isinstance(amount, int) or amount <= 0:
            raise ValueError("Amount must be a positive integer.")
        if amount > self.quantity:
            raise ValueError("Not enough quantity in stock.")
        self.quantity -= amount
        if self.quantity == 0 and not isinstance(self, NonStockedProduct):
            self.active = False
        return self.price * amount

    def set_quantity(self, quantity: int) -> None:
        """
        Set a new quantity for the product. Automatically deactivate if quantity reaches 0.

        :param quantity: new quantity to set
        """
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a non-negative integer.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def deactivate(self) -> None:
        """Set the product as not active."""
        self.active = False

    def activate(self) -> None:
        """Set the product as active."""
        self.active = True

    def show(self):
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Active: {self.active}"

    def is_active(self):
        return self.active

    def get_quantity(self):
        """Return the current quantity of the product."""
        return self.quantity


class NonStockedProduct(Product):

    """A product that does not require stock tracking (e.g. digital license)-"""
    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)
        self.active = True # Always active, even if quantity is 0

    def set_quantity(self, quantity):
        self.quantity = 0 # Always zero, can not be changed

    def buy(self, quantity):
        if not isinstance(quantity, int) or quantity <= 0:
            raise Exception("Quantity must be a positive integer.")
        return quantity * self.price


class LimitedProduct(Product):
    """A product that can only be purchased in limited quantity per order"""

    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum # max quantity per purchase

    def buy(self, quantity):
        """Limit quantity per purchase."""
        if quantity > self.maximum:
            raise Exception(f"Cannot buy more than {self.maximum} of this product")
        return super().buy(quantity)

    def show(self):
        return (f"{self.name} (Price: {self.price}, Quantity: {self.quantity}, "
                f"Max per order: {self.maximum}, Active: {self.active})")

    def is_active(self):
        """Return True if product is active."""
        return self.active
