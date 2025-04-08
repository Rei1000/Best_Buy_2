from products import Product, LimitedProduct, NonStockedProduct
from store import Store
from promotions import PercentDiscount, SecondHalfPrice, ThirdOneFree

# setup initial stock of inventory
product_list = [
    Product("MacBook Air M2", price=1450, quantity=100),
    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    Product("Google Pixel 7", price=500, quantity=500),
    NonStockedProduct("Windows License", price=200),
    LimitedProduct("Shipping", price=10, quantity=5, maximum=1)  # ← dein Testfall
]

# Assign promotions to some products
product_list[0].set_promotion(PercentDiscount("20% off", percent=20))          # MacBook Air M2
product_list[1].set_promotion(SecondHalfPrice("Second one half price"))        # Bose Earbuds
product_list[2].set_promotion(ThirdOneFree("3 für 2 Aktion"))                  # Pixel 7

best_buy = Store(product_list)

def start(store):
    """
    Starts the interactive Best Buy store program.
    Displays a menu with options to:
    1. List all products
    2. Show total quantity in the store
    3. Make a purchase
    4. Quit the application
    """
    while True:
        print("\nPlease choose an option:")
        print("1. List of all products in the store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Enter your choice number (1-4): ")

        if choice not in["1", "2", "3", "4"]:
            print("Invalid input. Please enter a number from 1 to 4.")
            continue

        if choice == "1":
            # show all products including inactive ones
            for index, product in enumerate(store.products, start=1):
                print(f"{index}. {product.show()}")

        elif choice == "2":
            # Display total quantity of all products
            print("Total quantity in store:", store.get_total_quantity())

        elif choice == "3":
            # Allow user to make an order one by one
            order_list = []  # Collect (Product, quantity) tuples

            while True:
                planned_quantities = {}
                for prod, qty in order_list:
                    planned_quantities[prod] = planned_quantities.get(prod, 0) + qty

                # Show all products
                products_for_order = store.products
                print("\nAvailable products:")
                for index, product in enumerate(products_for_order, start=1):
                    planned = planned_quantities.get(product, 0)
                    if isinstance(product, NonStockedProduct):
                        available = 0
                    else:
                        available = product.get_quantity() - planned
                        # Aktualisiere den aktiven Status basierend auf der verfügbaren Menge
                        if available == 0:
                            product.deactivate()
                        else:
                            product.activate()

                    promotion_info = f", Promotion: {product.promotion.name}" if product.promotion else ""
                    print(f"{index}. {product.name} (Quantity available: {available}, Active: {product.is_active()}{promotion_info})")

                # choose product index
                index_input = input("Enter the product number you want to order (or 'q' to cancel): ").strip()
                if index_input.lower() == 'q':
                    print("Order cancelled.")
                    break
                if not index_input.isdigit():
                    print("Invalid input. Please enter a valid number.")
                    continue

                index = int(index_input)
                if index < 1 or index > len(products_for_order):
                    print("Product index out of range.")
                    continue

                selected_product = products_for_order[index - 1]

                if not selected_product.is_active():
                    print(f"The selected product '{selected_product.name}' is inactive and cannot be ordered.")
                    continue

                planned = planned_quantities.get(selected_product, 0)
                available = selected_product.get_quantity() - planned

                if available <= 0 and not isinstance(selected_product, NonStockedProduct):
                    print(f"Sorry, {selected_product.name} is out of stock.")
                    continue

                # choose quantity
                while True:
                    if isinstance(selected_product, LimitedProduct) and selected_product.maximum == 1:
                        print(f"Note: {selected_product.name} can only be ordered 1 per order.")
                    if not selected_product.is_active():
                        print(f"The product '{selected_product.name}' is inactive and cannot be ordered.")
                        break

                    planned = planned_quantities.get(selected_product, 0)
                    available = selected_product.get_quantity() - planned
                    quantity_input = input(f"Enter quantity for {selected_product.name} (or 'q' to cancel): ").strip()
                    if quantity_input.lower() == "q":
                        print("Order cancelled.")
                        return
                    if not quantity_input.isdigit():
                        print("Invalid quantity. Please enter a number.")
                        continue

                    quantity = int(quantity_input)

                    # Überprüfung: Bei LimitedProduct darf nicht mehr als das Maximum bestellt werden
                    if isinstance(selected_product, LimitedProduct):
                        if quantity > selected_product.maximum:
                            print(f"Cannot order more than {selected_product.maximum} of this product.")
                            continue

                    if quantity > available and not isinstance(selected_product, NonStockedProduct):
                        print(
                            f"Not enough quantity in stock. Maximum available is {available}. Please enter a smaller amount.")
                        continue

                    break  # valid quantity

                order_list.append((selected_product, quantity))
                # Update active status of the selected product immediately after ordering
                if not isinstance(selected_product, NonStockedProduct) and selected_product.get_quantity() == 0:
                    selected_product.deactivate()

                # Ask if the user wants to add another product
                another_product = input("Would you like to add another product? (y/n): ").strip().lower()
                if another_product == 'n':
                    # process the order
                    try:
                        total = store.order(order_list)
                        # Synchronize active status after ordering
                        for product in store.products:
                            if not isinstance(product, NonStockedProduct):
                                if product.get_quantity() == 0:
                                    product.deactivate()
                                else:
                                    product.activate()
                        print("\nOrder successful! Summary:")
                        print(f"{'Product':30} {'Unit Price':>12} {'Quantity':>10} {'Subtotal':>12}")
                        for product, quantity in order_list:
                            subtotal = product.promotion.apply_promotion(product, quantity) if product.promotion else product.price * quantity
                            print(f"{product.name:30} {product.price:12} €{quantity:10} "
                                  f"{subtotal:12} €")
                        print("-" * 70)
                        print(f"{'Total':>54} {total:12} €")
                    except Exception as e:
                        raise Exception("Order failed") from e
                    break

        elif choice == "4":
            print("Goodbye!")
            break


if __name__ == "__main__":
    """ 
    Main entry point of the Best Buy application.
    Initializes the store and handles clean exit on keyboard interruption.
    """
    try:
        start(best_buy)
    except KeyboardInterrupt:
        print("\n\nProgram interrupted. Goodbye!")
