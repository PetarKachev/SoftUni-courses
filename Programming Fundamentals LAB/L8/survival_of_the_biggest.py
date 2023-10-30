numbers_list = input().split(" ")

numbers_int = []

for num in numbers_list:
    numbers_int.append(int(num))

remover = int(input())

for num1 in range(remover):
    numbers_int.remove(min(numbers_int))

print(", ".join(map(str, numbers_int)))