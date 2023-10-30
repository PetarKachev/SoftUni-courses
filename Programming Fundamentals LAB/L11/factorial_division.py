first_number = int(input())
second_number = int(input())

def factorial(first, second):
    factorial1 = 1
    factorial2 = 1
    result_of_deviding = 0
    for num in range(1, first + 1):
        factorial1 = factorial1 * num

    for num1 in range(1, second + 1):
        factorial2 = factorial2 * num1

    result_of_deviding = factorial1 / factorial2
    print(f'{float(result_of_deviding):.2f}')

factorial(first_number, second_number)