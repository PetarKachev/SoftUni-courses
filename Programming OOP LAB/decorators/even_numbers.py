def even_numbers(function):

    def wrapper(numbers):
        result = [el for el in numbers if el % 2 == 0]
        return function(result)

    return wrapper