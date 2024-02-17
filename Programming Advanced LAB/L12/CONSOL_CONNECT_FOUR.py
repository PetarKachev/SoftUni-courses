def verification(board, current_row, current_col):

    if board[current_row][current_col] == 1:
        first_row_count = board[current_row][0:4].count(1)
        second_row_count = board[current_row][1:5].count(1)
        third_row_count = board[current_row][2:6].count(1)
        forth_row_count = board[current_row][3:7].count(1)

        if first_row_count == 4 or second_row_count == 4 or third_row_count == 4 or forth_row_count == 4:
            print("First player wins the game")
            exit()

        first_col_count = []
        second_col_count = []
        third_col_count = []
        for row in range(0, len(board) - 2):
            first_col_count.append(board[row][current_col])
        for row in range(1, len(board) - 1):
            second_col_count.append(board[row][current_col])
        for row in range(2, len(board)):
            third_col_count.append(board[row][current_col])

        first_col_count = first_col_count.count(1)
        second_col_count = second_col_count.count(1)
        third_col_count = third_col_count.count(1)

        if first_col_count == 4 or second_col_count == 4 or third_col_count == 4:
            print("First player wins the game")
            exit()

        first_diagonal_count = [board[5][3], board[4][4], board[3][5], board[2][6]].count(1)
        second_diagonal_count = [board[5][2], board[4][3], board[3][4], board[2][5]].count(1)
        third_diagonal_count = [board[4][3], board[3][4], board[2][5], board[1][6]].count(1)
        forth_diagonal_count = [board[5][1], board[4][2], board[3][3], board[2][4]].count(1)
        fifth_diagonal_count = [board[4][2], board[3][3], board[2][4], board[1][5]].count(1)
        sixth_diagonal_count = [board[3][3], board[2][4], board[1][5], board[0][6]].count(1)
        seventh_diagonal_count = [board[5][0], board[4][1], board[3][2], board[2][3]].count(1)
        eight_diagonal_count = [board[4][1], board[3][2], board[2][3], board[1][4]].count(1)
        ninth_diagonal_count = [board[3][2], board[2][3], board[1][4], board[0][5]].count(1)
        tenth_diagonal_count = [board[4][0], board[3][1], board[2][2], board[1][3]].count(1)
        eleventh_diagonal_count = [board[3][1], board[2][2], board[1][3], board[0][4]].count(1)
        twelfth_diagonal_count = [board[3][0], board[2][1], board[1][2], board[0][3]].count(1)

        thirteen_diagonal_count = [board[5][3], board[4][2], board[3][1], board[2][0]].count(1)
        fortheen_diagonal_count = [board[5][4], board[4][3], board[3][2], board[2][1]].count(1)
        fiftheen_diagonal_count = [board[4][3], board[3][2], board[2][1], board[1][0]].count(1)
        sixtheen_diagonal_count = [board[5][5], board[4][4], board[3][3], board[2][2]].count(1)
        seventheen_diagonal_count = [board[4][4], board[3][3], board[2][2], board[1][1]].count(1)
        eighteen_diagonal_count = [board[3][3], board[2][2], board[1][1], board[0][0]].count(1)
        ninetheen_diagonal_count = [board[5][6], board[4][5], board[3][4], board[2][3]].count(1)
        twenty_diagonal_count = [board[4][5], board[3][4], board[2][3], board[1][2]].count(1)
        twenty_one_diagonal_count = [board[3][4], board[2][3], board[1][2], board[0][1]].count(1)
        twenty_two_diagonal_count = [board[4][6], board[3][5], board[2][4], board[1][3]].count(1)
        twenty_three_diagonal_count = [board[3][5], board[2][4], board[1][3], board[0][2]].count(1)
        twenty_four_diagonal_count = [board[3][6], board[2][5], board[1][4], board[0][3]].count(1)

        if first_diagonal_count == 4 or second_diagonal_count == 4 or third_diagonal_count == 4 or forth_diagonal_count == 4 or fifth_diagonal_count == 4 or sixth_diagonal_count == 4 or seventh_diagonal_count == 4 or eight_diagonal_count == 4 or ninth_diagonal_count == 4 or tenth_diagonal_count == 4 or eleventh_diagonal_count == 4 or twelfth_diagonal_count == 4 or thirteen_diagonal_count == 4 or fortheen_diagonal_count == 4 or fiftheen_diagonal_count == 4 or sixtheen_diagonal_count == 4 or seventheen_diagonal_count == 4 or eighteen_diagonal_count == 4 or ninetheen_diagonal_count == 4 or twenty_diagonal_count == 4 or twenty_one_diagonal_count == 4 or twenty_two_diagonal_count == 4 or twenty_three_diagonal_count == 4 or twenty_four_diagonal_count == 4:
            print("First player wins the game")
            exit()

    elif board[current_row][current_col] == 2:

        first_row_count = board[current_row][0:4].count(2)
        second_row_count = board[current_row][1:5].count(2)
        third_row_count = board[current_row][2:6].count(2)
        forth_row_count = board[current_row][3:7].count(2)

        if first_row_count == 4 or second_row_count == 4 or third_row_count == 4 or forth_row_count == 4:
            print("Second player wins the game")
            exit()

        first_col_count = []
        second_col_count = []
        third_col_count = []
        for row in range(0, len(board) - 2):
            first_col_count.append(board[row][current_col])
        for row in range(1, len(board) - 1):
            second_col_count.append(board[row][current_col])
        for row in range(2, len(board)):
            third_col_count.append(board[row][current_col])

        first_col_count = first_col_count.count(2)
        second_col_count = second_col_count.count(2)
        third_col_count = third_col_count.count(2)

        if first_col_count == 4 or second_col_count == 4 or third_col_count == 4:
            print("Second player wins the game")
            exit()

        first_diagonal_count = [board[5][3], board[4][4], board[3][5], board[2][6]].count(2)
        second_diagonal_count = [board[5][2], board[4][3], board[3][4], board[2][5]].count(2)
        third_diagonal_count = [board[4][3], board[3][4], board[2][5], board[1][6]].count(2)
        forth_diagonal_count = [board[5][1], board[4][2], board[3][3], board[2][4]].count(2)
        fifth_diagonal_count = [board[4][2], board[3][3], board[2][4], board[1][5]].count(2)
        sixth_diagonal_count = [board[3][3], board[2][4], board[1][5], board[0][6]].count(2)
        seventh_diagonal_count = [board[5][0], board[4][1], board[3][2], board[2][3]].count(2)
        eight_diagonal_count = [board[4][1], board[3][2], board[2][3], board[1][4]].count(2)
        ninth_diagonal_count = [board[3][2], board[2][3], board[1][4], board[0][5]].count(2)
        tenth_diagonal_count = [board[4][0], board[3][1], board[2][2], board[1][3]].count(2)
        eleventh_diagonal_count = [board[3][1], board[2][2], board[1][3], board[0][4]].count(2)
        twelfth_diagonal_count = [board[3][0], board[2][1], board[1][2], board[0][3]].count(2)

        thirteen_diagonal_count = [board[5][3], board[4][2], board[3][1], board[2][0]].count(2)
        fortheen_diagonal_count = [board[5][4], board[4][3], board[3][2], board[2][1]].count(2)
        fiftheen_diagonal_count = [board[4][3], board[3][2], board[2][1], board[1][0]].count(2)
        sixtheen_diagonal_count = [board[5][5], board[4][4], board[3][3], board[2][2]].count(2)
        seventheen_diagonal_count = [board[4][4], board[3][3], board[2][2], board[1][1]].count(2)
        eighteen_diagonal_count = [board[3][3], board[2][2], board[1][1], board[0][0]].count(2)
        ninetheen_diagonal_count = [board[5][6], board[4][5], board[3][4], board[2][3]].count(2)
        twenty_diagonal_count = [board[4][5], board[3][4], board[2][3], board[1][2]].count(2)
        twenty_one_diagonal_count = [board[3][4], board[2][3], board[1][2], board[0][1]].count(2)
        twenty_two_diagonal_count = [board[4][6], board[3][5], board[2][4], board[1][3]].count(2)
        twenty_three_diagonal_count = [board[3][5], board[2][4], board[1][3], board[0][2]].count(2)
        twenty_four_diagonal_count = [board[3][6], board[2][5], board[1][4], board[0][3]].count(2)

        if first_diagonal_count == 4 or second_diagonal_count == 4 or third_diagonal_count == 4 or forth_diagonal_count == 4 or fifth_diagonal_count == 4 or sixth_diagonal_count == 4 or seventh_diagonal_count == 4 or eight_diagonal_count == 4 or ninth_diagonal_count == 4 or tenth_diagonal_count == 4 or eleventh_diagonal_count == 4 or twelfth_diagonal_count == 4 or thirteen_diagonal_count == 4 or fortheen_diagonal_count == 4 or fiftheen_diagonal_count == 4 or sixtheen_diagonal_count == 4 or seventheen_diagonal_count == 4 or eighteen_diagonal_count == 4 or ninetheen_diagonal_count == 4 or twenty_diagonal_count == 4 or twenty_one_diagonal_count == 4 or twenty_two_diagonal_count == 4 or twenty_three_diagonal_count == 4 or twenty_four_diagonal_count == 4:
            print("Second player wins the game")
            exit()

rows = 6
columns = 7
board = []
for row in range(rows):
    board.append(columns * [0])
column_full = False

while True:
    try:
        first_player_move = input("Player 1, please choose a column")
        first_player_move = int(first_player_move) - 1

        if 0 <= first_player_move < columns:
            for row in range(row, - 1, -1):
                if board[0][first_player_move] == 0:
                    if board[row][first_player_move] == 0:
                        board[row][first_player_move] = 1
                        row = 5
                        verification(board, row, first_player_move)
                        break
                    else:
                        continue
                else:
                    print("Column is full, please choose again")
                    column_full = True
                    break
        else:
            print("Column out of range, please try again")
            continue
    except ValueError:
        print("Invalid input, please insert a valid column number next time, you lost your turn")

    if column_full == True:
        row = 5
        column_full = False
        continue
    else:
        column_full = False

    try:
        second_player_move = input("Player 2, please choose a column")
        second_player_move = int(second_player_move) - 1

        if 0 <= second_player_move < columns:
            for row in range(row, -1, -1):
                if board[row][second_player_move] == 0:
                    board[row][second_player_move] = 2
                    row = 5
                    verification(board, row, first_player_move)
                    break
                else:
                    continue
        else:
            print("Column out of range, please try again")
            continue
    except ValueError:
        print("Invalid input, please insert a valid column number next time, you lost your turn")