rows = int(input())
matrix = []
for row in range(rows):
    data = list(map(int, input().split(", ")))
    for element in data:
        matrix.append(element)
print(matrix)