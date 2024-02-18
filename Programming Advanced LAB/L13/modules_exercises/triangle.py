num = int(input())

for row in range(1, num + 2):
    for nested_row in range(1, row):
        print(nested_row, end=" ")
    print()

for row in range(num, 0, -1):
    for nested_row in range(1, row):
        print(nested_row, end=" ")
    print()