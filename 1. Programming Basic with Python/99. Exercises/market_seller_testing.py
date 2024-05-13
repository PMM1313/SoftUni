# market_seller_testing.py
from market_stall import Product
first_prod = Product("Coffee", 1.1, 2.5, 30)
second_prod = Product("Chocolate", 0.9, 1.75, 35)

first_prod.show_stock()
second_prod.show_stock()

first_prod.decrease_stock(7)

print()

first_prod.show_stock()
second_prod.show_stock()
