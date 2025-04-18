from project import Food


class Dessert(Food):
    def __init__(self, name: str, price: int, grams: float, calories: float):
        super().__init__(name, price, grams)
        self.__calories = calories
        
    @property
    def calories(self):
        return self.__calories