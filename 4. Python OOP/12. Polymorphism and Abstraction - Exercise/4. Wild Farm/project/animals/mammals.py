from typing import List, Type

from project import Mammal
from project import Food, Vegetable, Fruit, Meat


class Mouse(Mammal):
    @staticmethod
    def make_sound():
        return "Squeak"

    @property
    def allowed_food(self) -> List[Type[Food]]:
        return [Fruit, Vegetable]

    @property
    def weight_coefficient(self) -> float:
        return 0.1


class Dog(Mammal):

    @staticmethod
    def make_sound():
        return "Woof!"

    @property
    def allowed_food(self) -> List[Type[Food]]:
        return [Meat]

    @property
    def weight_coefficient(self) -> float:
        return 0.4


class Cat(Mammal):
    @staticmethod
    def make_sound():
        return "Meow"

    @property
    def allowed_food(self) -> List[Type[Food]]:
        return [Meat, Vegetable]

    @property
    def weight_coefficient(self) -> float:
        return 0.3


class Tiger(Mammal):
    @staticmethod
    def make_sound():
        return "ROAR!!!"

    @property
    def allowed_food(self) -> List[Type[Food]]:
        return [Meat]

    @property
    def weight_coefficient(self) -> float:
        return 1.0

