from products import Product
from store import Store
mac = Product("MacBook Air M2", price=1450, quantity=100)
bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
samsung = Product("Samsung Galaxy Buds", price=120, quantity=700)

store = Store([mac, bose])
store.add_product(samsung)
store.remove_product(bose)

print("Total quantity:", store.get_total_quantity())
print("Active products:", [p.name for p in store.get_all_products()])
print("Total order price:", store.order([(mac, 1), (samsung, 2)]))