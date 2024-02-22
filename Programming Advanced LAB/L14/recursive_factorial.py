def get_factorial(num):
    if num == 0:
        return 1

    return num * get_factorial(num - 1)