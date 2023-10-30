import sys

first_number = int(input())
second_number = int(input())

max_number = - sys.maxsize

for i in range(1, second_number + 1):
    if i % first_number == 0 and i > max_number:
        max_number = i

print(max_number)