first_int = int(input())
second_int = int(input())
third_int = int(input())

def sum_numbers(first, second):
    return first + second

def subtract(first, second, third):
    return (first + second) - third

def add_and_subtract(first, second, third):
    return subtract(first, second, third)

print(add_and_subtract(first_int, second_int, third_int))