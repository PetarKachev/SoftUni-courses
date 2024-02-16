rows, cols = input().split(", ")
rows = int(rows)
cols = int(cols)
matrix = []
player = []
all_elements = 0

christmas_decorations = 0
gifts = 0
cookies = 0

for row in range(rows):
    data = input().split(" ")
    matrix.append(data)

    for element in range(len(data)):
        if data[element] == "Y":
            player.append(row)
            player.append(element)
        elif data[element] == "D" or data[element] == "G" or data[element] == "C":
            all_elements += 1
command = input()

while command != "End" and all_elements > 0:
    command = command.split("-")

    if command[0] == "right":
        steps = int(command[1])

        while steps > 0:
            matrix[player[0]][player[1]] = "x"

            if 0 <= player[1] + 1 < cols:
                next_element = matrix[player[0]][player[1] + 1]
                player[1] += 1

                if next_element == ".":
                    matrix[player[0]][player[1]] = "Y"

                elif next_element == "x":
                    matrix[player[0]][player[1]] = "Y"

                elif next_element == "D":
                    matrix[player[0]][player[1]] = "Y"
                    christmas_decorations += 1
                    all_elements -= 1
                    if all_elements == 0:
                        print("Merry Christmas!")
                        break

                elif next_element == "G":
                    matrix[player[0]][player[1]] = "Y"
                    gifts += 1
                    all_elements -= 1
                    if all_elements == 0:
                        print("Merry Christmas!")
                        break

                elif next_element == "C":
                    matrix[player[0]][player[1]] = "Y"
                    cookies += 1
                    all_elements -= 1
                    if all_elements == 0:
                        print("Merry Christmas!")
                        break

            else:
                player[1] = 0
                next_element = matrix[player[0]][player[1]]

                if next_element == ".":
                    matrix[player[0]][player[1]] = "Y"

                elif next_element == "x":
                    matrix[player[0]][player[1]] = "Y"

                elif next_element == "D":
                    matrix[player[0]][player[1]] = "Y"
                    christmas_decorations += 1
                    all_elements -= 1
                    if all_elements == 0:
                        print("Merry Christmas!")
                        break

                elif next_element == "G":
                    matrix[player[0]][player[1]] = "Y"
                    gifts += 1
                    all_elements -= 1
                    if all_elements == 0:
                        print("Merry Christmas!")
                        break

                elif next_element == "C":
                    matrix[player[0]][player[1]] = "Y"
                    cookies += 1
                    all_elements -= 1
                    if all_elements == 0:
                        print("Merry Christmas!")
                        break
            steps -= 1

    elif command[0] == "left":
        steps = int(command[1])

        while steps > 0:
            matrix[player[0]][player[1]] = "x"

            if 0 <= player[1] - 1 < cols:
                next_element = matrix[player[0]][player[1] - 1]
                player[1] -= 1

                if next_element == ".":
                    matrix[player[0]][player[1]] = "Y"

                elif next_element == "x":
                    matrix[player[0]][player[1]] = "Y"

                elif next_element == "D":
                    matrix[player[0]][player[1]] = "Y"
                    christmas_decorations += 1
                    all_elements -= 1
                    if all_elements == 0:
                        print("Merry Christmas!")
                        break

                elif next_element == "G":
                    matrix[player[0]][player[1]] = "Y"
                    gifts += 1
                    all_elements -= 1
                    if all_elements == 0:
                        print("Merry Christmas!")
                        break

                elif next_element == "C":
                    matrix[player[0]][player[1]] = "Y"
                    cookies += 1
                    all_elements -= 1
                    if all_elements == 0:
                        print("Merry Christmas!")
                        break

            else:
                player[1] = cols - 1
                next_element = matrix[player[0]][player[1]]

                if next_element == ".":
                    matrix[player[0]][player[1]] = "Y"

                elif next_element == "x":
                    matrix[player[0]][player[1]] = "Y"

                elif next_element == "D":
                    matrix[player[0]][player[1]] = "Y"
                    christmas_decorations += 1
                    all_elements -= 1
                    if all_elements == 0:
                        print("Merry Christmas!")
                        break

                elif next_element == "G":
                    matrix[player[0]][player[1]] = "Y"
                    gifts += 1
                    all_elements -= 1
                    if all_elements == 0:
                        print("Merry Christmas!")
                        break

                elif next_element == "C":
                    matrix[player[0]][player[1]] = "Y"
                    cookies += 1
                    all_elements -= 1
                    if all_elements == 0:
                        print("Merry Christmas!")
                        break
            steps -= 1

    elif command[0] == "up":
        steps = int(command[1])

        while steps > 0:
            matrix[player[0]][player[1]] = "x"

            if 0 <= player[0] - 1 < rows:
                next_element = matrix[player[0] - 1][player[1]]
                player[0] -= 1

                if next_element == ".":
                    matrix[player[0]][player[1]] = "Y"

                elif next_element == "x":
                    matrix[player[0]][player[1]] = "Y"

                elif next_element == "D":
                    matrix[player[0]][player[1]] = "Y"
                    christmas_decorations += 1
                    all_elements -= 1
                    if all_elements == 0:
                        print("Merry Christmas!")
                        break

                elif next_element == "G":
                    matrix[player[0]][player[1]] = "Y"
                    gifts += 1
                    all_elements -= 1
                    if all_elements == 0:
                        print("Merry Christmas!")
                        break

                elif next_element == "C":
                    matrix[player[0]][player[1]] = "Y"
                    cookies += 1
                    all_elements -= 1
                    if all_elements == 0:
                        print("Merry Christmas!")
                        break

            else:
                player[0] = rows - 1
                next_element = matrix[player[0]][player[1]]

                if next_element == ".":
                    matrix[player[0]][player[1]] = "Y"

                elif next_element == "x":
                    matrix[player[0]][player[1]] = "Y"

                elif next_element == "D":
                    matrix[player[0]][player[1]] = "Y"
                    christmas_decorations += 1
                    all_elements -= 1
                    if all_elements == 0:
                        print("Merry Christmas!")
                        break

                elif next_element == "G":
                    matrix[player[0]][player[1]] = "Y"
                    gifts += 1
                    all_elements -= 1
                    if all_elements == 0:
                        print("Merry Christmas!")
                        break

                elif next_element == "C":
                    matrix[player[0]][player[1]] = "Y"
                    cookies += 1
                    all_elements -= 1
                    if all_elements == 0:
                        print("Merry Christmas!")
                        break
            steps -= 1

    elif command[0] == "down":
        steps = int(command[1])

        while steps > 0:
            matrix[player[0]][player[1]] = "x"

            if 0 <= player[0] + 1 < rows:
                next_element = matrix[player[0] + 1][player[1]]
                player[0] += 1

                if next_element == ".":
                    matrix[player[0]][player[1]] = "Y"

                elif next_element == "x":
                    matrix[player[0]][player[1]] = "Y"

                elif next_element == "D":
                    matrix[player[0]][player[1]] = "Y"
                    christmas_decorations += 1
                    all_elements -= 1
                    if all_elements == 0:
                        print("Merry Christmas!")
                        break

                elif next_element == "G":
                    matrix[player[0]][player[1]] = "Y"
                    gifts += 1
                    all_elements -= 1
                    if all_elements == 0:
                        print("Merry Christmas!")
                        break

                elif next_element == "C":
                    matrix[player[0]][player[1]] = "Y"
                    cookies += 1
                    all_elements -= 1
                    if all_elements == 0:
                        print("Merry Christmas!")
                        break

            else:
                player[0] = 0
                next_element = matrix[player[0]][player[1]]

                if next_element == ".":
                    matrix[player[0]][player[1]] = "Y"

                elif next_element == "x":
                    matrix[player[0]][player[1]] = "Y"

                elif next_element == "D":
                    matrix[player[0]][player[1]] = "Y"
                    christmas_decorations += 1
                    all_elements -= 1
                    if all_elements == 0:
                        print("Merry Christmas!")
                        break

                elif next_element == "G":
                    matrix[player[0]][player[1]] = "Y"
                    gifts += 1
                    all_elements -= 1
                    if all_elements == 0:
                        print("Merry Christmas!")
                        break

                elif next_element == "C":
                    matrix[player[0]][player[1]] = "Y"
                    cookies += 1
                    all_elements -= 1
                    if all_elements == 0:
                        print("Merry Christmas!")
                        break
            steps -= 1
    if all_elements == 0:
        break
    command = input()

print("You've collected:")
print(f'- {christmas_decorations} Christmas decorations')
print(f'- {gifts} Gifts')
print(f'- {cookies} Cookies')
for element in matrix:
    print(' '.join(element))