class Product:
    """This class represents a product with name, price, quantity, and active status."""

    def __init__(self, name, price=0.0, quantity=0): #Constructor
        """Create a new product and check if the values are valid"""

        if not isinstance(name, str) or not name.strip():
            raise Exception("Name must be a non-empty string.")
        # check for string and not empty

        if not isinstance(price, (int, float)) or price <= 0:
            raise Exception("Price must be greater than 0.")
        # check for int or float and greater than 0

        if not isinstance(quantity, int) or quantity <= 0:
            raise Exception("Quantity must be a non-negative integer.")
        #check for int and greater than 0

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True


    def set_quantity(self, quantity):
        """Set a new quantity for the product. Deactivate it if quantity is 0."""

        if not isinstance(quantity, int) or quantity < 0:
            raise Exception("Quantity must be a non-negative integer.")
        # check for int greater than 0

        self.quantity = quantity

        if quantity == 0:
            self.active = False


    def activate(self):
        """Set the product as active."""
        return self.active

    def deactivate(self):
        """Set the product as not active."""
        self.active = False


    def get_quantity(self):
        """Return the current quantity of the product."""
        return self.quantity

    def is_active(self):
        """Return True if the product is active, otherwise False."""
        return self.active


    def show(self):
        """Return a string that shows the product details."""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity} (Active: {self.active})"


    def buy(self,quantity):
        """Buy a number of items. Update stock and return total price."""

        if not isinstance(quantity, int) or quantity <= 0:
            raise Exception("Quantity to buy must be bigger than 0")
        # Check if requested quantity is a positive number

        if quantity > self.quantity:
            # Check if enough items are in stock
            raise Exception("Not enough parts in stock to complete purchase.")

        self.quantity -= quantity
        # Subtract bought quantity

        if self.quantity == 0:
            self.active = False
            # Deactivate product if quantity becomes 0
        return quantity * self.price
