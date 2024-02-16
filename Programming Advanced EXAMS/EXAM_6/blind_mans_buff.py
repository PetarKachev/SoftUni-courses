info = input().split()
rows = int(info[0])
cols = int(info[1])
matrix = []
player = []
touched_oponent = 0
number_moves = 0
for row in range(rows):
    data = list(map(str, input().split()))
    matrix.append(data)
    for element in range(len(data)):
        if data[element] == "B":
            player.append(row)
            player.append(element)

command = input()
while command != "Finish":

    if command == "up":
        if 0 <= player[0] - 1 < rows:
            if matrix[player[0] - 1][player[1]] == "-":
                matrix[player[0]][player[1]] = "-"
                player[0] -= 1
                matrix[player[0]][player[1]] = "B"
                number_moves += 1
            elif matrix[player[0] - 1][player[1]] == "P":
                matrix[player[0]][player[1]] = "-"
                player[0] -= 1
                matrix[player[0]][player[1]] = "B"
                number_moves += 1
                touched_oponent += 1
                if touched_oponent == 3:
                    break

    elif command == "down":
        if 0 <= player[0] + 1 < rows:
            if matrix[player[0] + 1][player[1]] == "-":
                matrix[player[0]][player[1]] = "-"
                player[0] += 1
                matrix[player[0]][player[1]] = "B"
                number_moves += 1
            elif matrix[player[0] + 1][player[1]] == "P":
                matrix[player[0]][player[1]] = "-"
                player[0] += 1
                matrix[player[0]][player[1]] = "B"
                number_moves += 1
                touched_oponent += 1
                if touched_oponent == 3:
                    break

    elif command == "right":
        if 0 <= player[1] + 1 < rows:
            if matrix[player[0]][player[1] + 1] == "-":
                matrix[player[0]][player[1]] = "-"
                player[1] += 1
                matrix[player[0]][player[1]] = "B"
                number_moves += 1
            elif matrix[player[0]][player[1] + 1] == "P":
                matrix[player[0]][player[1]] = "-"
                player[1] += 1
                matrix[player[0]][player[1]] = "B"
                number_moves += 1
                touched_oponent += 1
                if touched_oponent == 3:
                    break

    elif command == "left":
        if 0 <= player[1] - 1 < rows:
            if matrix[player[0]][player[1] - 1] == "-":
                matrix[player[0]][player[1]] = "-"
                player[1] -= 1
                matrix[player[0]][player[1]] = "B"
                number_moves += 1
            elif matrix[player[0]][player[1] - 1] == "P":
                matrix[player[0]][player[1]] = "-"
                player[1] -= 1
                matrix[player[0]][player[1]] = "B"
                number_moves += 1
                touched_oponent += 1
                if touched_oponent == 3:
                    break
    command = input()

print("Game over!")
print(f"Touched opponents: {touched_oponent} Moves made: {number_moves}")