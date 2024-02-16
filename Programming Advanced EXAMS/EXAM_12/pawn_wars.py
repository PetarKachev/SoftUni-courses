rows = 8
columns = 8
matrix = []
white_pos = []
black_pos = []
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
real_board = []
counter = 0

for num in range(rows, - 1, - 1):
    current_row = []
    for letter in letters:
        current_row.append(f'{letter}{num}')
    real_board.append(current_row)
    counter += 1
    if counter == 8:
        break

for row in range(rows):
    data = input().split(" ")
    matrix.append(data)
    for element in range(len(data)):
        if data[element] == "w":
            white_pos.append(row)
            white_pos.append(element)
        elif data[element] == "b":
            black_pos.append(row)
            black_pos.append(element)


while True:

    if 0 <= white_pos[0] - 1 < 8 and 0 <= white_pos[1] - 1 < 8:
        if matrix[white_pos[0] - 1][white_pos[1] - 1] == "b":
            white_pos[0] -= 1
            white_pos[1] -= 1
            print(f"Game over! White win, capture on {real_board[white_pos[0]][white_pos[1]]}.")
            exit()

    if 0 <= white_pos[0] - 1 < 8 and 0 <= white_pos[1] + 1 < 8:
        if matrix[white_pos[0] - 1][white_pos[1] + 1] == "b":
            white_pos[0] -= 1
            white_pos[1] += 1
            print(f"Game over! White win, capture on {real_board[white_pos[0]][white_pos[1]]}.")
            exit()

    if matrix[white_pos[0] - 1][white_pos[1]] == "-":
        matrix[white_pos[0]][white_pos[1]] = "-"
        white_pos[0] -= 1
        matrix[white_pos[0]][white_pos[1]] = "w"
        if white_pos[0] == 0:
            print(f"Game over! White pawn is promoted to a queen at {real_board[white_pos[0]][white_pos[1]]}.")
            exit()

    if 0 <= black_pos[0] + 1 < 8 and 0 <= black_pos[1] - 1 < 8:
        if matrix[black_pos[0] + 1][black_pos[1] - 1] == "w":
            black_pos[0] += 1
            black_pos[1] -= 1
            print(f"Game over! Black win, capture on {real_board[black_pos[0]][black_pos[1]]}.")
            exit()

    if 0 <= black_pos[0] + 1 < 8 and 0 <= black_pos[1] + 1 < 8:
        if matrix[black_pos[0] + 1][black_pos[1] + 1] == "w":
            black_pos[0] += 1
            black_pos[1] += 1
            print(f"Game over! Black win, capture on {real_board[black_pos[0]][black_pos[1]]}.")
            exit()

    if matrix[black_pos[0] + 1][black_pos[1]] == "-":
        matrix[black_pos[0]][black_pos[1]] = "-"
        black_pos[0] += 1
        matrix[black_pos[0]][black_pos[1]] = "b"
        if black_pos[0] == 7:
            print(f"Game over! Black pawn is promoted to a queen at {real_board[black_pos[0]][black_pos[1]]}.")
            exit()