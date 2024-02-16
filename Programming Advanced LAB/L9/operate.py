def operate(operator, *args):

    def add():
        result = int(args[0])
        for element in range(1, len(args)):
            result += int(args[element])
        return result

    def multiplication():
        result = int(args[0])
        for element in range(1, len(args)):
            result *= int(args[element])
        return result

    def subtraction():
        result = int(args[0])
        for element in range(1, len(args)):
            result -= int(args[element])
        return result

    def division():
        result = int(args[0])
        for element in range(1, len(args)):
            result /= int(args[element])
        return result

    if operator == "+":
        return add()
    elif operator == "-":
        return subtraction()
    elif operator == "*":
        return multiplication()
    elif operator == "/":
        return division()