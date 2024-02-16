rows = int(input())
movements = list(map(str, input().split(" ")))
all_coals = 0
matrix = []
miner_position = []
final_coal_pos = [0, 0]

for row in range(rows):
    data = list(map(str, input().split(" ")))
    matrix.append(data)
    for element in range(len(data)):
        if data[element] == "c":
            all_coals += 1
        elif data[element] == "s":
            miner_position.append(row)
            miner_position.append(element)

for element in movements:
    len_matrix = rows
    len_column = len(matrix[0])

    if element == "up":
        matrix[miner_position[0]][miner_position[1]] = "*"
        next_position = miner_position[0] - 1

        if 0 <= next_position < len_matrix:

            if matrix[miner_position[0] - 1][miner_position[1]] == "*":
                miner_position[0] -= 1
                matrix[miner_position[0]][miner_position[1]] = 's'

            elif matrix[miner_position[0] - 1][miner_position[1]] == "e":
                miner_position[0] -= 1
                matrix[miner_position[0]][miner_position[1]] = 's'
                print(f"Game over! ({miner_position[0]}, {miner_position[1]})")
                exit()

            elif matrix[miner_position[0] - 1][miner_position[1]] == "c":
                miner_position[0] -= 1
                matrix[miner_position[0]][miner_position[1]] = 's'
                all_coals -= 1
                if all_coals == 0:
                    break

    elif element == "down":
        matrix[miner_position[0]][miner_position[1]] = "*"
        next_position = miner_position[0] + 1

        if 0 <= next_position < len_matrix:

            if matrix[miner_position[0] + 1][miner_position[1]] == "*":
                miner_position[0] += 1
                matrix[miner_position[0]][miner_position[1]] = 's'

            elif matrix[miner_position[0] + 1][miner_position[1]] == "e":
                miner_position[0] += 1
                matrix[miner_position[0]][miner_position[1]] = 's'
                print(f"Game over! ({miner_position[0]}, {miner_position[1]})")
                exit()

            elif matrix[miner_position[0] + 1][miner_position[1]] == "c":
                miner_position[0] += 1
                matrix[miner_position[0]][miner_position[1]] = 's'
                all_coals -= 1
                if all_coals == 0:
                    break

    elif element == "right":
        matrix[miner_position[0]][miner_position[1]] = "*"
        next_position = miner_position[1] + 1

        if 0 <= next_position < len_column:

            if matrix[miner_position[0]][miner_position[1] + 1] == "*":
                miner_position[1] += 1
                matrix[miner_position[0]][miner_position[1]] = 's'

            elif matrix[miner_position[0]][miner_position[1] + 1] == "e":
                miner_position[1] += 1
                matrix[miner_position[0]][miner_position[1]] = 's'
                print(f"Game over! ({miner_position[0]}, {miner_position[1]})")
                exit()

            elif matrix[miner_position[0]][miner_position[1] + 1] == "c":
                miner_position[1] += 1
                matrix[miner_position[0]][miner_position[1]] = 's'
                all_coals -= 1
                if all_coals == 0:
                    break

    elif element == "left":
        matrix[miner_position[0]][miner_position[1]] = "*"
        next_position = miner_position[1] - 1

        if 0 <= next_position < len_column:

            if matrix[miner_position[0]][miner_position[1] - 1] == "*":
                miner_position[1] -= 1
                matrix[miner_position[0]][miner_position[1]] = 's'

            elif matrix[miner_position[0]][miner_position[1] - 1] == "e":
                miner_position[1] -= 1
                matrix[miner_position[0]][miner_position[1]] = 's'
                print(f"Game over! ({miner_position[0]}, {miner_position[1]})")
                exit()

            elif matrix[miner_position[0]][miner_position[1] - 1] == "c":
                miner_position[1] -= 1
                matrix[miner_position[0]][miner_position[1]] = 's'
                all_coals -= 1
                if all_coals == 0:
                    break

if all_coals == 0:
    print(f"You collected all coal! ({miner_position[0]}, {miner_position[1]})")
else:
    print(f"{all_coals} pieces of coal left. ({miner_position[0]}, {miner_position[1]})")