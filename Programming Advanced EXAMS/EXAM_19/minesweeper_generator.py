rows = int(input())
bombs = int(input())
matrix = []

for row in range(rows):
    matrix.append(rows * ['0'])

for current_bomb in range(bombs):
    position = input()
    current_row = int(position[1])
    current_col = int(position[4])
    matrix[current_row][current_col] = "*"

for row in range(len(matrix)):
    for col in range(len(matrix[row])):

        current_number_bombs = 0

        if 0 <= row - 1 < rows and 0 <= col - 1 < rows:
            if matrix[row - 1][col - 1] == '*':
                current_number_bombs += 1

        if 0 <= row - 1 < rows and 0 <= col < rows:
            if matrix[row - 1][col] == '*':
                current_number_bombs += 1

        if 0 <= row - 1 < rows and 0 <= col + 1 < rows:
            if matrix[row - 1][col + 1] == '*':
                current_number_bombs += 1

        if 0 <= row < rows and 0 <= col - 1 < rows:
            if matrix[row][col - 1] == '*':
                current_number_bombs += 1

        if 0 <= row < rows and 0 <= col + 1 < rows:
            if matrix[row][col + 1] == '*':
                current_number_bombs += 1

        if 0 <= row + 1 < rows and 0 <= col - 1 < rows:
            if matrix[row + 1][col - 1] == '*':
                current_number_bombs += 1

        if 0 <= row + 1 < rows and 0 <= col < rows:
            if matrix[row + 1][col] == '*':
                current_number_bombs += 1

        if 0 <= row + 1 < rows and 0 <= col + 1 < rows:
            if matrix[row + 1][col + 1] == '*':
                current_number_bombs += 1

        if matrix[row][col] != "*":
            matrix[row][col] = f'{current_number_bombs}'

for element in matrix:
    print(' '.join(element))