import math
from math import floor


class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if not isinstance(float_value, float):
            return "value is not a float"
        return cls(math.floor(float_value))

    @classmethod
    def from_roman(cls, value):
        if not isinstance(value, str) or not value.isalpha() or not value.isupper():
            return "value is not a valid Roman numeral"
        decimal_value = 0
        numeral_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        for i in range(len(value) - 1):
            if numeral_values[value[i]] >= numeral_values[value[i + 1]]:
                decimal_value += numeral_values[value[i]]
            else:
                decimal_value -= numeral_values[value[i]]
        decimal_value += numeral_values[value[-1]]
        return cls(decimal_value)

    @classmethod
    def from_string(cls, value):
        if not isinstance(value, str):
            return "wrong type"
        try:
            return cls(int(value))
        except ValueError:
            return "wrong type"