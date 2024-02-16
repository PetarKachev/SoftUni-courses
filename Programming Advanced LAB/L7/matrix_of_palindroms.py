info = list(map(int, input().split(" ")))
rows = info[0]
columns = info[1]
matrix = []

for row in range(rows):
    matrix.append([])
    for col in range(columns):
        matrix[row].append(f'{chr(97 + row)}{chr(97 + row + col)}{chr(97 + row)}')

for element in matrix:
    print(' '.join(element))