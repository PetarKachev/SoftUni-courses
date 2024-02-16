rows = int(input())
matrix = []
for i in range(rows):
    data = input()
    matrix.append([])
    matrix[i].append(data)
symbol = input()
position = []

for row in range(len(matrix)):
    for element in range(len(matrix[row][0])):
        if matrix[row][0][element] == symbol:
            position.append(row)
            position.append(element)

if len(position) > 0:
    print(f'{position[0], position[1]}')
else:
    print(f"{symbol} does not occur in the matrix")