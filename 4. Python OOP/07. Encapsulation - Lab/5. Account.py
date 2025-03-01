class Account:
    def __init__(self, id, balance, pin):
        self.__id = id
        self.balance = balance
        self.__pin = pin

    def get_id(self, pin):
        if self.__pin == pin:
            return self.__id
        return "Wrong pin"

    def change_pin(self, old, new):
        if self.__pin == old:
            self.__pin = new
            return "Pin changed"
        return "Wrong pin"