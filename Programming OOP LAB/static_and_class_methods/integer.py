from math import floor


class Integer:

    roman_symbols = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if not isinstance(float_value, float):
            return "value is not a float"
        else:
            return cls(int(floor(float_value)))

    @classmethod
    def from_roman(cls, value):

        result = 0

        for i in range(len(value)):
            if i != 0 and Integer.roman_symbols[value[i]] > Integer.roman_symbols[value[i - 1]]:
                result += Integer.roman_symbols[value[i]] - 2 * Integer.roman_symbols[value[i - 1]]
            else:
                result += Integer.roman_symbols[value[i]]
        value = result
        return cls(int(value))

    @classmethod
    def from_string(cls, value):
        if not isinstance(value, str):
            return "wrong type"
        else:
            return cls(int(value))