class Inventory:
    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.items = []

    def add_item(self, item: str):
        if len(self.items) < self.__capacity:
            self.items.append(item)
        else:
            return "not enough room in the inventory"

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        left_capacity = self.__capacity - len(self.items)
        items_str = ", ".join(self.items)
        return f"Items: {items_str}.\nCapacity left: {left_capacity}"

# Test code
inventory = Inventory(2)
print(inventory.add_item("potion"))  # Output: None (item added successfully)
print(inventory.add_item("sword"))   # Output: None (item added successfully)
print(inventory.add_item("bottle"))  # Output: "not enough room in the inventory"
print(inventory.get_capacity())     # Output: 2
print(inventory)                    # Output: Items: potion, sword.
                                    #         Capacity left: 0