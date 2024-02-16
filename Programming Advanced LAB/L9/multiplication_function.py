def multiply(*args):
    result = 1
    for element in args:
        result *= int(element)
    return result