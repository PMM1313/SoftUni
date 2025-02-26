from typing import Union


class Account:
    def __init__(self, _id, name: str, balance: int = 0):
        self.id = _id
        self.name = name
        self.balance = balance

    def credit(self, amount: int):
        self.balance += amount
        return self.balance

    def debit(self, amount: int) -> Union[int, str]:
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        else:
            return "Amount exceeded balance"

    def info(self):
        return f"User {self.name} with account {self.id} has {self.balance} balance"