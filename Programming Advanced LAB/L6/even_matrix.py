rows = int(input())

matrix = []

for current_row in range(rows):
    data = list(map(int, input().split(", ")))
    matrix.append([])
    for element in data:
        if element % 2 == 0:
            matrix[current_row].append(element)

print(matrix)