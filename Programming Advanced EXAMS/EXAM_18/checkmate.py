rows = 8
cols = 8
matrix = []
queens = []
winner_queens = []

for row in range(rows):
    data = input().split(" ")
    matrix.append(data)
    for element in range(len(data)):
        if data[element] == "Q":
            queens.append([row, element])

for queen in queens:
    row = queen[0]
    col = queen[1]

    for cur_element in range(len(matrix[row])):
        if cur_element > col:
            if matrix[row][cur_element] == "Q":
                break
            elif matrix[row][cur_element] == "K":
                winner_queens.append(queen)
                break

    for cur_element in range(len(matrix[row]), -1, -1):
        if cur_element < col:
            if matrix[row][cur_element] == "Q":
                break
            elif matrix[row][cur_element] == "K":
                winner_queens.append(queen)
                break

    for cur_element in range(len(matrix)):
        if cur_element > row:
            if matrix[cur_element][col] == "Q":
                break
            elif matrix[cur_element][col] == "K":
                winner_queens.append(queen)
                break

    for cur_element in range(len(matrix), -1, -1):
        if cur_element < row:
            if matrix[cur_element][col] == "Q":
                break
            elif matrix[cur_element][col] == "K":
                winner_queens.append(queen)
                break

    col = queen[1]
    for cur_element in range(len(matrix)):

        if cur_element > row:

            col += 1
            if col > 7:
                break
            if matrix[cur_element][col] == "Q":
                break
            elif matrix[cur_element][col] == "K":
                winner_queens.append(queen)
                break

    col = queen[1]
    for cur_element in range(len(matrix), -1, -1):

        if cur_element < row:

            col += 1
            if col > 7:
                break
            if matrix[cur_element][col] == "Q":
                break
            elif matrix[cur_element][col] == "K":
                winner_queens.append(queen)
                break

    col = queen[1]
    for cur_element in range(len(matrix)):

        if cur_element > row:

            col -= 1
            if col == 0:
                break
            if matrix[cur_element][col] == "Q":
                break
            elif matrix[cur_element][col] == "K":
                winner_queens.append(queen)
                break

    col = queen[1]
    for cur_element in range(len(matrix), -1, -1):

        if cur_element < row:

            col -= 1
            if col == 0:
                break
            if matrix[cur_element][col] == "Q":
                break
            elif matrix[cur_element][col] == "K":
                winner_queens.append(queen)
                break

if len(winner_queens) == 0:
    print("The king is safe!")
else:
    for element in winner_queens:
        print(element)