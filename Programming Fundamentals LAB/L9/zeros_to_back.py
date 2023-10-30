string = input().split(", ")

integer_list = []

for i in string:
    integer_list.append(int(i))

numbers = []
zeros = []

for num in integer_list:
    if num > 0:
        numbers.append(num)
    else:
        zeros.append(num)

for num1 in zeros:
    numbers.append(num1)

print(numbers)