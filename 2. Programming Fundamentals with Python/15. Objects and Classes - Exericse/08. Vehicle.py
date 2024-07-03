class Vehicle:
    def __init__(self, type: str, model: str, price: float):
        self.type = type
        self.model = model
        self.price = price
        self.owner = None

    def buy(self, money: float, owner: str):
        if self.owner is not None:
            return "Car already sold"

        if money >= self.price:
            change = money - self.price
            self.owner = owner
            return f"Successfully bought a {self.type}. Change: {change:.2f}"
        else:
            return "Sorry, not enough money"

    def sell(self):
        if self.owner is not None:
            self.owner = None
        else:
            return "Vehicle has no owner"

    def __repr__(self):
        if self.owner is not None:
            return f"{self.model} {self.type} is owned by: {self.owner}"
        else:
            return f"{self.model} {self.type} is on sale: {int(self.price)}"


# Example usage:
vehicle_type = "car"
model = "BMW"
price = 30000.00
vehicle = Vehicle(vehicle_type, model, price)

print(vehicle.buy(15000.00, "Peter"))
print(vehicle.buy(35000.00, "George"))
print(vehicle)

vehicle.sell()
print(vehicle)