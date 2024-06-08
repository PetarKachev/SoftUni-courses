rows = 6
cols = 6
matrix = []
for row in range(rows):
    data = input().split()
    matrix.append(data)

player = input()
player_pos = [int(player[1]), int(player[4])]
command = input()
while command != "Stop":
    command = command.split(", ")

    if command[0] == "Create":
        direction = command[1]
        value = command[2]
        if direction == "up":

            if 0 <= player_pos[0] - 1 < rows:
                if matrix[player_pos[0] - 1][player_pos[1]] == ".":
                    player_pos[0] -= 1
                    matrix[player_pos[0]][player_pos[1]] = value
                else:
                    player_pos[0] -= 1

        elif direction == "down":

            if 0 <= player_pos[0] + 1 < rows:
                if matrix[player_pos[0] + 1][player_pos[1]] == ".":
                    player_pos[0] += 1
                    matrix[player_pos[0]][player_pos[1]] = value
                else:
                    player_pos[0] += 1

        elif direction == "right":

            if 0 <= player_pos[1] + 1 < cols:
                if matrix[player_pos[0]][player_pos[1] + 1] == ".":
                    player_pos[1] += 1
                    matrix[player_pos[0]][player_pos[1]] = value
                else:
                    player_pos[1] += 1

        elif direction == "left":

            if 0 <= player_pos[1] - 1 < cols:
                if matrix[player_pos[0]][player_pos[1] - 1] == ".":
                    player_pos[1] -= 1
                    matrix[player_pos[0]][player_pos[1]] = value
                else:
                    player_pos[1] -= 1

    elif command[0] == "update":
        direction = command[1]
        value = command[2]
        if direction == "up":

            if 0 <= player_pos[0] - 1 < rows:
                if matrix[player_pos[0] - 1][player_pos[1]].isdigit():
                    player_pos[0] -= 1
                    matrix[player_pos[0]][player_pos[1]] = value
                elif matrix[player_pos[0] - 1][player_pos[1]].isalpha():
                    player_pos[0] -= 1
                    matrix[player_pos[0]][player_pos[1]] = value
                else:
                    player_pos[0] -= 1

        elif direction == "down":

            if 0 <= player_pos[0] + 1 < rows:
                if matrix[player_pos[0] + 1][player_pos[1]].isdigit():
                    player_pos[0] += 1
                    matrix[player_pos[0]][player_pos[1]] = value
                elif matrix[player_pos[0] + 1][player_pos[1]].isalpha():
                    player_pos[0] += 1
                    matrix[player_pos[0]][player_pos[1]] = value
                else:
                    player_pos[0] += 1

        elif direction == "right":

            if 0 <= player_pos[1] + 1 < cols:
                if matrix[player_pos[0]][player_pos[1] + 1].isdigit():
                    player_pos[1] += 1
                    matrix[player_pos[0]][player_pos[1]] = value
                elif matrix[player_pos[0]][player_pos[1] + 1].isalpha():
                    player_pos[1] += 1
                    matrix[player_pos[0]][player_pos[1]] = value
                else:
                    player_pos[1] += 1

        elif direction == "left":

            if 0 <= player_pos[1] - 1 < cols:
                if matrix[player_pos[0]][player_pos[1] - 1].isdigit():
                    player_pos[1] -= 1
                    matrix[player_pos[0]][player_pos[1]] = value
                elif matrix[player_pos[0]][player_pos[1] - 1].isalpha():
                    player_pos[1] -= 1
                    matrix[player_pos[0]][player_pos[1]] = value
                else:
                    player_pos[1] -= 1

    elif command[0] == "delete":
        direction = command[1]
        if direction == "up":

            if 0 <= player_pos[0] - 1 < rows:
                if matrix[player_pos[0] - 1][player_pos[1]].isdigit():
                    player_pos[0] -= 1
                    matrix[player_pos[0]][player_pos[1]] = "."
                elif matrix[player_pos[0] - 1][player_pos[1]].isalpha():
                    player_pos[0] -= 1
                    matrix[player_pos[0]][player_pos[1]] = "."
                else:
                    player_pos[0] -= 1

        elif direction == "down":

            if 0 <= player_pos[0] + 1 < rows:
                if matrix[player_pos[0] + 1][player_pos[1]].isdigit():
                    player_pos[0] += 1
                    matrix[player_pos[0]][player_pos[1]] = "."
                elif matrix[player_pos[0] + 1][player_pos[1]].isalpha():
                    player_pos[0] += 1
                    matrix[player_pos[0]][player_pos[1]] = "."
                else:
                    player_pos[0] += 1

        elif direction == "right":

            if 0 <= player_pos[1] + 1 < cols:
                if matrix[player_pos[0]][player_pos[1] + 1].isdigit():
                    player_pos[1] += 1
                    matrix[player_pos[0]][player_pos[1]] = "."
                elif matrix[player_pos[0]][player_pos[1] + 1].isalpha():
                    player_pos[1] += 1
                    matrix[player_pos[0]][player_pos[1]] = "."
                else:
                    player_pos[1] += 1

        elif direction == "left":

            if 0 <= player_pos[1] - 1 < cols:
                if matrix[player_pos[0]][player_pos[1] - 1].isdigit():
                    player_pos[1] -= 1
                    matrix[player_pos[0]][player_pos[1]] = "."
                elif matrix[player_pos[0]][player_pos[1] - 1].isalpha():
                    player_pos[1] -= 1
                    matrix[player_pos[0]][player_pos[1]] = "."
                else:
                    player_pos[1] -= 1

    elif command[0] == "Read":
        direction = command[1]
        if direction == "up":

            if 0 <= player_pos[0] - 1 < rows:
                if matrix[player_pos[0] - 1][player_pos[1]].isdigit():
                    player_pos[0] -= 1
                    print(matrix[player_pos[0]][player_pos[1]])
                elif matrix[player_pos[0] - 1][player_pos[1]].isalpha():
                    player_pos[0] -= 1
                    print(matrix[player_pos[0]][player_pos[1]])
                else:
                    player_pos[0] -= 1

        elif direction == "down":

            if 0 <= player_pos[0] + 1 < rows:
                if matrix[player_pos[0] + 1][player_pos[1]].isdigit():
                    player_pos[0] += 1
                    print(matrix[player_pos[0]][player_pos[1]])
                elif matrix[player_pos[0] + 1][player_pos[1]].isalpha():
                    player_pos[0] += 1
                    print(matrix[player_pos[0]][player_pos[1]])
                else:
                    player_pos[0] += 1

        elif direction == "right":

            if 0 <= player_pos[1] + 1 < cols:
                if matrix[player_pos[0]][player_pos[1] + 1].isdigit():
                    player_pos[1] += 1
                    print(matrix[player_pos[0]][player_pos[1]])
                elif matrix[player_pos[0]][player_pos[1] + 1].isalpha():
                    player_pos[1] += 1
                    print(matrix[player_pos[0]][player_pos[1]])
                else:
                    player_pos[1] += 1

        elif direction == "left":

            if 0 <= player_pos[1] - 1 < cols:
                if matrix[player_pos[0]][player_pos[1] - 1].isdigit():
                    player_pos[1] -= 1
                    print(matrix[player_pos[0]][player_pos[1]])
                elif matrix[player_pos[0]][player_pos[1] - 1].isalpha():
                    player_pos[1] -= 1
                    print(matrix[player_pos[0]][player_pos[1]])
                else:
                    player_pos[1] -= 1
    command = input()
for element in matrix:
    print(' '.join(element))