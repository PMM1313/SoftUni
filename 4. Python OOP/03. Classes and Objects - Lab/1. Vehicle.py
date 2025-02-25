class Vehicle:
    def __init__(self, mileage: int, max_speed=150):
        self.max_speed = max_speed
        self.mileage = mileage
        self.gadgets = []


car = Vehicle(20)
print(car.mileage)
print(car.max_speed)