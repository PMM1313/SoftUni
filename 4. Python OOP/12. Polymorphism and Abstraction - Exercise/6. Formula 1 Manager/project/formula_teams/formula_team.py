from abc import ABC, abstractmethod
from typing import Tuple, Dict


class FormulaTeam(ABC):
    BUDGET = 1000000

    def __init__(self, budget):
        self.budget = budget

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        if value < self.BUDGET:
            raise ValueError("F1 is expensive sport, find more sponsors!")
        self.__budget = value


    @property
    @abstractmethod
    def team_data(self) -> Tuple[int, Dict[str, Dict[int, int]]]:
        pass

    def calculate_revenue_after_race(self, race_pos):
        expenses, sponsors = self.team_data
        revenue = 0

        for sponsors in sponsors.values():
            for position, money in sponsors.items():
                if position <= position:
                    revenue += money
                    break

        revenue -= expenses
        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"