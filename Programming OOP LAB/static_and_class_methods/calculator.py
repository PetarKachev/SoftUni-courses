from functools import reduce


class Calculator:

    def add(*args):
        return sum([*args])

    def multiply(*args):
        return reduce(lambda a, b: a * b, [*args])

    def divide(*args):
        return reduce(lambda a, b: a / b, [*args])

    def subtract(*args):
        return reduce(lambda a, b: a - b, [*args])