class Weapon:
    def __init__(self, bullets):
        self.bullets = bullets

    def shoot(self):
        if self.bullets > 0:
            self.bullets -= 1
            return "shooting..."
        else:
            return "no bullets left"

    def __repr__(self):
        return f"Remaining bullets: {self.bullets}"

# Test code
weapon = Weapon(5)
print(weapon.shoot())  # Output: shooting...
print(weapon.shoot())  # Output: shooting...
print(weapon)          # Output: Remaining bullets: 3
print(weapon.shoot())  # Output: shooting...
print(weapon.shoot())  # Output: shooting...
print(weapon.shoot())  # Output: shooting...
print(weapon.shoot())  # Output: no bullets left
print(weapon)          # Output: Remaining bullets: 0