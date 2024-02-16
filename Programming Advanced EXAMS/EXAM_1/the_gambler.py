rows = int(input())
matrix = []
amount = 100
g_pos = []

for row in range(rows):
    data = list(input())
    matrix.append(data)
    for element in range(len(data)):
        if data[element] == "G":
            g_pos.append(row)
            g_pos.append(element)
len_cols = len(matrix[0])
command = input()
jackpot_won = False

while command != "end":

    if command == "up":
        if 0 <= g_pos[0] - 1 < rows:
            matrix[g_pos[0]][g_pos[1]] = "-"
            if matrix[g_pos[0] - 1][g_pos[1]] == "-":
                matrix[g_pos[0] - 1][g_pos[1]] = "G"
                g_pos[0] -= 1
            elif matrix[g_pos[0] - 1][g_pos[1]] == "W":
                matrix[g_pos[0] - 1][g_pos[1]] = "G"
                g_pos[0] -= 1
                amount += 100
            elif matrix[g_pos[0] - 1][g_pos[1]] == "P":
                matrix[g_pos[0] - 1][g_pos[1]] = "G"
                g_pos[0] -= 1
                amount -= 200
                if amount <= 0:
                    print("Game over! You lost everything!")
                    exit()
            elif matrix[g_pos[0] - 1][g_pos[1]] == "J":
                matrix[g_pos[0] - 1][g_pos[1]] = "G"
                g_pos[0] -= 1
                amount += 100000
                jackpot_won = True
                break
        else:
            print("Game over! You lost everything!")
            exit()

    elif command == "down":
        if 0 <= g_pos[0] + 1 < rows:
            matrix[g_pos[0]][g_pos[1]] = "-"
            if matrix[g_pos[0] + 1][g_pos[1]] == "-":
                matrix[g_pos[0] + 1][g_pos[1]] = "G"
                g_pos[0] += 1
            elif matrix[g_pos[0] + 1][g_pos[1]] == "W":
                matrix[g_pos[0] + 1][g_pos[1]] = "G"
                g_pos[0] += 1
                amount += 100
            elif matrix[g_pos[0] + 1][g_pos[1]] == "P":
                matrix[g_pos[0] + 1][g_pos[1]] = "G"
                g_pos[0] += 1
                amount -= 200
                if amount <= 0:
                    print("Game over! You lost everything!")
                    exit()
            elif matrix[g_pos[0] + 1][g_pos[1]] == "J":
                matrix[g_pos[0] + 1][g_pos[1]] = "G"
                g_pos[0] += 1
                amount += 100000
                jackpot_won = True
                break
        else:
            print("Game over! You lost everything!")
            exit()

    elif command == "right":
        if 0 <= g_pos[1] + 1 < len_cols:
            matrix[g_pos[0]][g_pos[1]] = "-"
            if matrix[g_pos[0]][g_pos[1] + 1] == "-":
                matrix[g_pos[0]][g_pos[1] + 1] = "G"
                g_pos[1] += 1
            elif matrix[g_pos[0]][g_pos[1] + 1] == "W":
                matrix[g_pos[0]][g_pos[1] + 1] = "G"
                g_pos[1] += 1
                amount += 100
            elif matrix[g_pos[0]][g_pos[1] + 1] == "P":
                matrix[g_pos[0]][g_pos[1] + 1] = "G"
                g_pos[1] += 1
                amount -= 200
                if amount <= 0:
                    print("Game over! You lost everything!")
                    exit()
            elif matrix[g_pos[0]][g_pos[1] + 1] == "J":
                matrix[g_pos[0]][g_pos[1] + 1] = "G"
                g_pos[1] += 1
                amount += 100000
                jackpot_won = True
                break
        else:
            print("Game over! You lost everything!")
            exit()

    elif command == "left":
        if 0 <= g_pos[1] - 1 < len_cols:
            matrix[g_pos[0]][g_pos[1]] = "-"
            if matrix[g_pos[0]][g_pos[1] - 1] == "-":
                matrix[g_pos[0]][g_pos[1] - 1] = "G"
                g_pos[1] -= 1
            elif matrix[g_pos[0]][g_pos[1] - 1] == "W":
                matrix[g_pos[0]][g_pos[1] - 1] = "G"
                g_pos[1] -= 1
                amount += 100
            elif matrix[g_pos[0]][g_pos[1] - 1] == "P":
                matrix[g_pos[0]][g_pos[1] - 1] = "G"
                g_pos[1] -= 1
                amount -= 200
                if amount <= 0:
                    print("Game over! You lost everything!")
                    exit()
            elif matrix[g_pos[0]][g_pos[1] - 1] == "J":
                matrix[g_pos[0]][g_pos[1] - 1] = "G"
                g_pos[1] -= 1
                amount += 100000
                jackpot_won = True
                break
        else:
            print("Game over! You lost everything!")
            exit()
    command = input()

if jackpot_won == True:
    print("You win the Jackpot!")
    print(f"End of the game. Total amount: {amount}$")
    for element in matrix:
        print(''.join(element))
else:
    print(f"End of the game. Total amount: {amount}$")
    for element in matrix:
        print(''.join(element))