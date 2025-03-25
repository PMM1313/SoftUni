from typing import List, Type

from project import Bird
from project import Food, Meat, Fruit, Vegetable, Seed


class Owl(Bird):

    @staticmethod
    def make_sound():
        return "Hoot Hoot"

    @property
    def allowed_food(self) -> List[Type[Food]]:
        return [Meat]

    @property
    def weight_coefficient(self) -> float:
        return 0.25


class Hen(Bird):

    @staticmethod
    def make_sound():
        return "Cluck"

    @property
    def allowed_food(self) -> List[Type[Food]]:
        return [Meat, Fruit, Vegetable, Seed]

    @property
    def weight_coefficient(self) -> float:
        return 0.35
