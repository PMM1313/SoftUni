class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.radius = diameter / 2

    def calculate_circumference(self):
        return 2 * Circle.__pi * self.radius

    def calculate_area(self):
        return Circle.__pi * self.radius ** 2

    def calculate_area_of_sector(self, angle):
        return (angle / 360) * Circle.__pi * self.radius ** 2

# Test code
circle = Circle(10)
angle = 5
print(f"{circle.calculate_circumference():.2f}")  # Output: 31.40
print(f"{circle.calculate_area():.2f}")           # Output: 78.50
print(f"{circle.calculate_area_of_sector(angle):.2f}")  # Output: 1.09