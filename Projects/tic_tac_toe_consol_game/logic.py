def verification(board, position, player, symbols):
    winner = False

    if position == "1":

        if board[0][0] == " ":
            board[0][0] = symbols[player]

            if board[0][0] == symbols[player] and board[0][1] == symbols[player] and board[0][2] == symbols[player]:
                winner = True

            elif board[1][0] == symbols[player] and board[1][1] == symbols[player] and board[1][2] == symbols[player]:
                winner = True

            elif board[2][0] == symbols[player] and board[2][1] == symbols[player] and board[2][2] == symbols[player]:
                winner = True

            elif board[0][0] == symbols[player] and board[1][0] == symbols[player] and board[2][0] == symbols[player]:
                winner = True

            elif board[0][1] == symbols[player] and board[1][1] == symbols[player] and board[2][1] == symbols[player]:
                winner = True

            elif board[0][2] == symbols[player] and board[1][2] == symbols[player] and board[2][2] == symbols[player]:
                winner = True

            elif board[0][0] == symbols[player] and board[1][1] == symbols[player] and board[2][2] == symbols[player]:
                winner = True

            elif board[0][2] == symbols[player] and board[1][1] == symbols[player] and board[2][0] == symbols[player]:
                winner = True

    elif position == "2":

        if board[0][1] == " ":
            board[0][1] = symbols[player]

            if board[0][0] == symbols[player] and board[0][1] == symbols[player] and board[0][2] == symbols[player]:
                winner = True

            elif board[1][0] == symbols[player] and board[1][1] == symbols[player] and board[1][2] == symbols[player]:
                winner = True

            elif board[2][0] == symbols[player] and board[2][1] == symbols[player] and board[2][2] == symbols[player]:
                winner = True

            elif board[0][0] == symbols[player] and board[1][0] == symbols[player] and board[2][0] == symbols[player]:
                winner = True

            elif board[0][1] == symbols[player] and board[1][1] == symbols[player] and board[2][1] == symbols[player]:
                winner = True

            elif board[0][2] == symbols[player] and board[1][2] == symbols[player] and board[2][2] == symbols[player]:
                winner = True

            elif board[0][0] == symbols[player] and board[1][1] == symbols[player] and board[2][2] == symbols[player]:
                winner = True

            elif board[0][2] == symbols[player] and board[1][1] == symbols[player] and board[2][0] == symbols[player]:
                winner = True

    elif position == "3":

        if board[0][2] == " ":
            board[0][2] = symbols[player]

            if board[0][0] == symbols[player] and board[0][1] == symbols[player] and board[0][2] == symbols[player]:
                winner = True

            elif board[1][0] == symbols[player] and board[1][1] == symbols[player] and board[1][2] == symbols[player]:
                winner = True

            elif board[2][0] == symbols[player] and board[2][1] == symbols[player] and board[2][2] == symbols[player]:
                winner = True

            elif board[0][0] == symbols[player] and board[1][0] == symbols[player] and board[2][0] == symbols[player]:
                winner = True

            elif board[0][1] == symbols[player] and board[1][1] == symbols[player] and board[2][1] == symbols[player]:
                winner = True

            elif board[0][2] == symbols[player] and board[1][2] == symbols[player] and board[2][2] == symbols[player]:
                winner = True

            elif board[0][0] == symbols[player] and board[1][1] == symbols[player] and board[2][2] == symbols[player]:
                winner = True

            elif board[0][2] == symbols[player] and board[1][1] == symbols[player] and board[2][0] == symbols[player]:
                winner = True

    elif position == "4":

        if board[1][0] == " ":
            board[1][0] = symbols[player]

            if board[0][0] == symbols[player] and board[0][1] == symbols[player] and board[0][2] == symbols[player]:
                winner = True

            elif board[1][0] == symbols[player] and board[1][1] == symbols[player] and board[1][2] == symbols[player]:
                winner = True

            elif board[2][0] == symbols[player] and board[2][1] == symbols[player] and board[2][2] == symbols[player]:
                winner = True

            elif board[0][0] == symbols[player] and board[1][0] == symbols[player] and board[2][0] == symbols[player]:
                winner = True

            elif board[0][1] == symbols[player] and board[1][1] == symbols[player] and board[2][1] == symbols[player]:
                winner = True

            elif board[0][2] == symbols[player] and board[1][2] == symbols[player] and board[2][2] == symbols[player]:
                winner = True

            elif board[0][0] == symbols[player] and board[1][1] == symbols[player] and board[2][2] == symbols[player]:
                winner = True

            elif board[0][2] == symbols[player] and board[1][1] == symbols[player] and board[2][0] == symbols[player]:
                winner = True

    elif position == "5":

        if board[1][1] == " ":
            board[1][1] = symbols[player]

            if board[0][0] == symbols[player] and board[0][1] == symbols[player] and board[0][2] == symbols[player]:
                winner = True

            elif board[1][0] == symbols[player] and board[1][1] == symbols[player] and board[1][2] == symbols[player]:
                winner = True

            elif board[2][0] == symbols[player] and board[2][1] == symbols[player] and board[2][2] == symbols[player]:
                winner = True

            elif board[0][0] == symbols[player] and board[1][0] == symbols[player] and board[2][0] == symbols[player]:
                winner = True

            elif board[0][1] == symbols[player] and board[1][1] == symbols[player] and board[2][1] == symbols[player]:
                winner = True

            elif board[0][2] == symbols[player] and board[1][2] == symbols[player] and board[2][2] == symbols[player]:
                winner = True

            elif board[0][0] == symbols[player] and board[1][1] == symbols[player] and board[2][2] == symbols[player]:
                winner = True

            elif board[0][2] == symbols[player] and board[1][1] == symbols[player] and board[2][0] == symbols[player]:
                winner = True

    elif position == "6":

        if board[1][2] == " ":
            board[1][2] = symbols[player]

            if board[0][0] == symbols[player] and board[0][1] == symbols[player] and board[0][2] == symbols[player]:
                winner = True

            elif board[1][0] == symbols[player] and board[1][1] == symbols[player] and board[1][2] == symbols[player]:
                winner = True

            elif board[2][0] == symbols[player] and board[2][1] == symbols[player] and board[2][2] == symbols[player]:
                winner = True

            elif board[0][0] == symbols[player] and board[1][0] == symbols[player] and board[2][0] == symbols[player]:
                winner = True

            elif board[0][1] == symbols[player] and board[1][1] == symbols[player] and board[2][1] == symbols[player]:
                winner = True

            elif board[0][2] == symbols[player] and board[1][2] == symbols[player] and board[2][2] == symbols[player]:
                winner = True

            elif board[0][0] == symbols[player] and board[1][1] == symbols[player] and board[2][2] == symbols[player]:
                winner = True

            elif board[0][2] == symbols[player] and board[1][1] == symbols[player] and board[2][0] == symbols[player]:
                winner = True

    elif position == "7":

        if board[2][0] == " ":
            board[2][0] = symbols[player]

            if board[0][0] == symbols[player] and board[0][1] == symbols[player] and board[0][2] == symbols[player]:
                winner = True

            elif board[1][0] == symbols[player] and board[1][1] == symbols[player] and board[1][2] == symbols[player]:
                winner = True

            elif board[2][0] == symbols[player] and board[2][1] == symbols[player] and board[2][2] == symbols[player]:
                winner = True

            elif board[0][0] == symbols[player] and board[1][0] == symbols[player] and board[2][0] == symbols[player]:
                winner = True

            elif board[0][1] == symbols[player] and board[1][1] == symbols[player] and board[2][1] == symbols[player]:
                winner = True

            elif board[0][2] == symbols[player] and board[1][2] == symbols[player] and board[2][2] == symbols[player]:
                winner = True

            elif board[0][0] == symbols[player] and board[1][1] == symbols[player] and board[2][2] == symbols[player]:
                winner = True

            elif board[0][2] == symbols[player] and board[1][1] == symbols[player] and board[2][0] == symbols[player]:
                winner = True

    elif position == "8":

        if board[2][1] == " ":
            board[2][1] = symbols[player]

            if board[0][0] == symbols[player] and board[0][1] == symbols[player] and board[0][2] == symbols[player]:
                winner = True

            elif board[1][0] == symbols[player] and board[1][1] == symbols[player] and board[1][2] == symbols[player]:
                winner = True

            elif board[2][0] == symbols[player] and board[2][1] == symbols[player] and board[2][2] == symbols[player]:
                winner = True

            elif board[0][0] == symbols[player] and board[1][0] == symbols[player] and board[2][0] == symbols[player]:
                winner = True

            elif board[0][1] == symbols[player] and board[1][1] == symbols[player] and board[2][1] == symbols[player]:
                winner = True

            elif board[0][2] == symbols[player] and board[1][2] == symbols[player] and board[2][2] == symbols[player]:
                winner = True

            elif board[0][0] == symbols[player] and board[1][1] == symbols[player] and board[2][2] == symbols[player]:
                winner = True

            elif board[0][2] == symbols[player] and board[1][1] == symbols[player] and board[2][0] == symbols[player]:
                winner = True

    elif position == "9":

        if board[2][2] == " ":
            board[2][2] = symbols[player]

            if board[0][0] == symbols[player] and board[0][1] == symbols[player] and board[0][2] == symbols[player]:
                winner = True

            elif board[1][0] == symbols[player] and board[1][1] == symbols[player] and board[1][2] == symbols[player]:
                winner = True

            elif board[2][0] == symbols[player] and board[2][1] == symbols[player] and board[2][2] == symbols[player]:
                winner = True

            elif board[0][0] == symbols[player] and board[1][0] == symbols[player] and board[2][0] == symbols[player]:
                winner = True

            elif board[0][1] == symbols[player] and board[1][1] == symbols[player] and board[2][1] == symbols[player]:
                winner = True

            elif board[0][2] == symbols[player] and board[1][2] == symbols[player] and board[2][2] == symbols[player]:
                winner = True

            elif board[0][0] == symbols[player] and board[1][1] == symbols[player] and board[2][2] == symbols[player]:
                winner = True

            elif board[0][2] == symbols[player] and board[1][1] == symbols[player] and board[2][0] == symbols[player]:
                winner = True

    result = ''

    for row in range(len(board)):
        current_symbols = []

        for col in range(len(board[row])):
            current_symbols.append(board[row][col])

        current_row_symbols = f'| {current_symbols[0]} | {current_symbols[1]} | {current_symbols[2]} |'
        result += f'{current_row_symbols}\n'

    if winner == True:
        print(f'{player} a gagné!')
        exit()

    else:
        is_draw = True

        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == " ":
                    is_draw = False

        if is_draw == True:
            print(f'Egal!')
            exit()
        else:
            return result