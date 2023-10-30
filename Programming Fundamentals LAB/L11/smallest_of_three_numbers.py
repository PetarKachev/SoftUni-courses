first_num = int(input())
second_num = int(input())
third_num = int(input())

def smallest(some_numbers: list):
    return min(some_numbers)

result = smallest([first_num, second_num, third_num])
print(result)