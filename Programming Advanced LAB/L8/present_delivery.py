number_presents = int(input())
rows = int(input())
santa_pos = []
all_kids = 0
matrix = []
for row in range(rows):
    data = list(map(str, input().split(" ")))
    matrix.append(data)
    for element in range(len(data)):
        if data[element] == "S":
            santa_pos.append(row)
            santa_pos.append(element)
        elif data[element] == "V":
            all_kids += 1
command = input()
len_column = len(matrix[0])

while command:
    if command == "Christmas morning":
        break

    if command == "up":
        if 0 <= santa_pos[0] - 1 < rows:
            matrix[santa_pos[0]][santa_pos[1]] = "-"

            if matrix[santa_pos[0] - 1][santa_pos[1]] == "V":
                santa_pos[0] -= 1
                matrix[santa_pos[0]][santa_pos[1]] = "S"
                number_presents -= 1
                if number_presents <= 0:
                    break

            elif matrix[santa_pos[0] - 1][santa_pos[1]] == "-":
                santa_pos[0] -= 1
                matrix[santa_pos[0]][santa_pos[1]] = "S"

            elif matrix[santa_pos[0] - 1][santa_pos[1]] == "X":
                santa_pos[0] -= 1
                matrix[santa_pos[0]][santa_pos[1]] = "S"

            elif matrix[santa_pos[0] - 1][santa_pos[1]] == "C":
                santa_pos[0] -= 1
                matrix[santa_pos[0]][santa_pos[1]] = "S"

                if matrix[santa_pos[0] - 1][santa_pos[1]] == "V" or matrix[santa_pos[0] - 1][santa_pos[1]] == "X":
                    matrix[santa_pos[0] - 1][santa_pos[1]] = "-"
                    number_presents -= 1
                if matrix[santa_pos[0] + 1][santa_pos[1]] == "V" or matrix[santa_pos[0] + 1][santa_pos[1]] == "X":
                    matrix[santa_pos[0] + 1][santa_pos[1]] = "-"
                    number_presents -= 1
                if matrix[santa_pos[0]][santa_pos[1] - 1] == "V" or matrix[santa_pos[0]][santa_pos[1] - 1] == "X":
                    matrix[santa_pos[0]][santa_pos[1] - 1] = "-"
                    number_presents -= 1
                if matrix[santa_pos[0]][santa_pos[1] + 1] == "V" or matrix[santa_pos[0]][santa_pos[1] + 1] == "X":
                    matrix[santa_pos[0]][santa_pos[1] + 1] = "-"
                    number_presents -= 1

    elif command == "down":
        if 0 <= santa_pos[0] + 1 < rows:
            matrix[santa_pos[0]][santa_pos[1]] = "-"

            if matrix[santa_pos[0] + 1][santa_pos[1]] == "V":
                santa_pos[0] += 1
                matrix[santa_pos[0]][santa_pos[1]] = "S"
                number_presents -= 1
                if number_presents <= 0:
                    break

            elif matrix[santa_pos[0] + 1][santa_pos[1]] == "-":
                santa_pos[0] += 1
                matrix[santa_pos[0]][santa_pos[1]] = "S"

            elif matrix[santa_pos[0] + 1][santa_pos[1]] == "X":
                santa_pos[0] += 1
                matrix[santa_pos[0]][santa_pos[1]] = "S"

            elif matrix[santa_pos[0] + 1][santa_pos[1]] == "C":
                santa_pos[0] += 1
                matrix[santa_pos[0]][santa_pos[1]] = "S"

                if matrix[santa_pos[0] - 1][santa_pos[1]] == "V" or matrix[santa_pos[0] - 1][santa_pos[1]] == "X":
                    matrix[santa_pos[0] - 1][santa_pos[1]] = "-"
                    number_presents -= 1
                if matrix[santa_pos[0] + 1][santa_pos[1]] == "V" or matrix[santa_pos[0] + 1][santa_pos[1]] == "X":
                    matrix[santa_pos[0] + 1][santa_pos[1]] = "-"
                    number_presents -= 1
                if matrix[santa_pos[0]][santa_pos[1] - 1] == "V" or matrix[santa_pos[0]][santa_pos[1] - 1] == "X":
                    matrix[santa_pos[0]][santa_pos[1] - 1] = "-"
                    number_presents -= 1
                if matrix[santa_pos[0]][santa_pos[1] + 1] == "V" or matrix[santa_pos[0]][santa_pos[1] + 1] == "X":
                    matrix[santa_pos[0]][santa_pos[1] + 1] = "-"
                    number_presents -= 1

    elif command == "right":
        if 0 <= santa_pos[1] + 1 < len_column:
            matrix[santa_pos[0]][santa_pos[1]] = "-"

            if matrix[santa_pos[0]][santa_pos[1] + 1] == "V":
                santa_pos[1] += 1
                matrix[santa_pos[0]][santa_pos[1]] = "S"
                number_presents -= 1
                if number_presents <= 0:
                    break

            elif matrix[santa_pos[0]][santa_pos[1] + 1] == "-":
                santa_pos[1] += 1
                matrix[santa_pos[0]][santa_pos[1]] = "S"

            elif matrix[santa_pos[0]][santa_pos[1] + 1] == "X":
                santa_pos[1] += 1
                matrix[santa_pos[0]][santa_pos[1]] = "S"

            elif matrix[santa_pos[0]][santa_pos[1] + 1] == "C":
                santa_pos[1] += 1
                matrix[santa_pos[0]][santa_pos[1]] = "S"

                if matrix[santa_pos[0] - 1][santa_pos[1]] == "V" or matrix[santa_pos[0] - 1][santa_pos[1]] == "X":
                    matrix[santa_pos[0] - 1][santa_pos[1]] = "-"
                    number_presents -= 1
                if matrix[santa_pos[0] + 1][santa_pos[1]] == "V" or matrix[santa_pos[0] + 1][santa_pos[1]] == "X":
                    matrix[santa_pos[0] + 1][santa_pos[1]] = "-"
                    number_presents -= 1
                if matrix[santa_pos[0]][santa_pos[1] - 1] == "V" or matrix[santa_pos[0]][santa_pos[1] - 1] == "X":
                    matrix[santa_pos[0]][santa_pos[1] - 1] = "-"
                    number_presents -= 1
                if matrix[santa_pos[0]][santa_pos[1] + 1] == "V" or matrix[santa_pos[0]][santa_pos[1] + 1] == "X":
                    matrix[santa_pos[0]][santa_pos[1] + 1] = "-"
                    number_presents -= 1

    elif command == "left":
        if 0 <= santa_pos[1] - 1 < len_column:
            matrix[santa_pos[0]][santa_pos[1]] = "-"

            if matrix[santa_pos[0]][santa_pos[1] - 1] == "V":
                santa_pos[1] -= 1
                matrix[santa_pos[0]][santa_pos[1]] = "S"
                number_presents -= 1
                if number_presents <= 0:
                    break

            elif matrix[santa_pos[0]][santa_pos[1] - 1] == "-":
                santa_pos[1] -= 1
                matrix[santa_pos[0]][santa_pos[1]] = "S"

            elif matrix[santa_pos[0]][santa_pos[1] - 1] == "X":
                santa_pos[1] -= 1
                matrix[santa_pos[0]][santa_pos[1]] = "S"

            elif matrix[santa_pos[0]][santa_pos[1] - 1] == "C":
                santa_pos[1] -= 1
                matrix[santa_pos[0]][santa_pos[1]] = "S"

                if matrix[santa_pos[0] - 1][santa_pos[1]] == "V" or matrix[santa_pos[0] - 1][santa_pos[1]] == "X":
                    matrix[santa_pos[0] - 1][santa_pos[1]] = "-"
                    number_presents -= 1
                if matrix[santa_pos[0] + 1][santa_pos[1]] == "V" or matrix[santa_pos[0] + 1][santa_pos[1]] == "X":
                    matrix[santa_pos[0] + 1][santa_pos[1]] = "-"
                    number_presents -= 1
                if matrix[santa_pos[0]][santa_pos[1] - 1] == "V" or matrix[santa_pos[0]][santa_pos[1] - 1] == "X":
                    matrix[santa_pos[0]][santa_pos[1] - 1] = "-"
                    number_presents -= 1
                if matrix[santa_pos[0]][santa_pos[1] + 1] == "V" or matrix[santa_pos[0]][santa_pos[1] + 1] == "X":
                    matrix[santa_pos[0]][santa_pos[1] + 1] = "-"
                    number_presents -= 1
    command = input()
left_nice_kids = 0

for element in matrix:
    for current_symbol in element:
        if current_symbol == "V":
            left_nice_kids += 1

if number_presents == 0 and left_nice_kids > 0:
    print("Santa ran out of presents!")
for element in matrix:
    print(' '.join(element))
if left_nice_kids == 0:
    print(f"Good job, Santa! {all_kids} happy nice kid/s.")
else:
    print(f"No presents for {left_nice_kids} nice kid/s.")