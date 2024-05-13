# market_stall.py
class Product:
    def __init__(self, name, cost_price, selling_price, number_in_stock):
        self.name = name
        self.cost_price = cost_price
        self.selling_price = selling_price
        self.number_in_stock = number_in_stock

    def decrease_stock(self, quantity):
        self.number_in_stock -= quantity

    def change_cost_price(self, new_price):
        self.cost_price = new_price

    def change_selling_price(self, new_price):
        self.selling_price = new_price

    def show_stock(self):
        print(f"{self.name} | Number in stock: {self.number_in_stock}")
