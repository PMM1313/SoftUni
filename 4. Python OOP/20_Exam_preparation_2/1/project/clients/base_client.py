from abc import ABC, abstractmethod
from math import floor


class BaseClient(ABC):
    def __init__(self, name: str, phone_number: str):
        self.phone_number = phone_number
        self.name = name
        self.discount = 0.0
        self.total_orders = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        stripped_value = value.strip()

        if len(stripped_value) < 2:
            raise ValueError("Name must be at least two characters long!")
        self.__name = value

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        if not value.isdigit():
            raise ValueError("Phone number can contain only digits!")
        self.__phone_number = value

    @abstractmethod
    def update_discount(self):
        pass

    def update_total_orders(self):
        self.total_orders += 1

    def client_details(self):
        return f"Client: {self.name}, " \
               f"Phone number: {self.phone_number}, " \
               f"Orders count: {self.total_orders}, " \
               f"Discount: {floor(self.discount)}%"


