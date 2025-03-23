from products import Product
class Store:
    """This class represents a store that holds and manages a list of products."""

    def __init__(self, products):
        """Initialize the store with a list of products"""
        # Check that products is a list
        if not isinstance(products, list):
            raise Exception("Expected a list of products.")

        # Check that all elements in the list are Product instances
        for product in products:
            if not isinstance(product, Product):
                raise Exception("All items must be Product objects.")

        self.products = products


    """Add a list of products to products"""
    def add_product(self, product):
        """Add a product to the store"""
        self.products.append(product)


    """Remove a product from products list"""
    def remove_product(self, product):
        # check for products list is not empty
        if product not in self.products:
            raise Exception ("Product not found in the list.")
        self.products.remove(product)


    """Returns the sum of all Products."""
    def get_total_quantity(self):
        total = 0
        for product in self.products:
            total += product.quantity
        return total


    """Returns a list of all active products"""
    def get_all_products(self):
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products


    """Create a list with tuple (Product and quantity) and return the total price"""
    def order(self, shopping_list):
        if not isinstance(shopping_list,list):
            raise Exception("Expected shopping_list to be a list.")

        for item in shopping_list:
            if not (
                    isinstance(item, tuple) and
                    len(item) == 2 and
                    isinstance(item[0], Product) and
                    isinstance(item[1], int)
            ):
                raise Exception("Each item in shopping_list must be a tuple of (Product, quantity.")

        total = 0
        for product, quantity in shopping_list:
            try:
                total += product.buy(quantity)
            except Exception as e:
                raise Exception(f"Error ordering product {product.name}: {e}")
        return total


