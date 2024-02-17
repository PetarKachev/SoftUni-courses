rows = int(input())
matrix = []
player = []
burrows = []
food = 0

for row in range(rows):
    data = list(input())
    matrix.append(data)

    for index in range(len(data)):
        if data[index] == "S":
            player.append(row)
            player.append(index)
        elif data[index] == "B":
            burrows.append([row, index])

command = input()

while command:

    if command == "right":

        if 0 <= player[1] + 1 < len(matrix[0]):
            matrix[player[0]][player[1]] = "."
            next_element = matrix[player[0]][player[1] + 1]
            player[1] += 1

            if next_element == "-":
                matrix[player[0]][player[1]] = "S"

            elif next_element == "*":
                matrix[player[0]][player[1]] = "S"
                food += 1
                if food >= 10:
                    print("You won! You fed the snake.")
                    break

            elif next_element == "B":
                matrix[player[0]][player[1]] = "."

                for element in burrows:
                    if element != player:
                        player = element

                matrix[player[0]][player[1]] = "S"

        else:
            matrix[player[0]][player[1]] = "."
            print("Game over!")
            break

    elif command == "left":

        if 0 <= player[1] - 1 < len(matrix[0]):
            matrix[player[0]][player[1]] = "."
            next_element = matrix[player[0]][player[1] - 1]
            player[1] -= 1

            if next_element == "-":
                matrix[player[0]][player[1]] = "S"

            elif next_element == "*":
                matrix[player[0]][player[1]] = "S"
                food += 1
                if food >= 10:
                    print("You won! You fed the snake.")
                    break

            elif next_element == "B":
                matrix[player[0]][player[1]] = "."

                for element in burrows:
                    if element != player:
                        player = element

                matrix[player[0]][player[1]] = "S"

        else:
            matrix[player[0]][player[1]] = "."
            print("Game over!")
            break

    elif command == "up":

        if 0 <= player[0] - 1 < len(matrix):
            matrix[player[0]][player[1]] = "."
            next_element = matrix[player[0] - 1][player[1]]
            player[0] -= 1

            if next_element == "-":
                matrix[player[0]][player[1]] = "S"

            elif next_element == "*":
                matrix[player[0]][player[1]] = "S"
                food += 1
                if food >= 10:
                    print("You won! You fed the snake.")
                    break

            elif next_element == "B":
                matrix[player[0]][player[1]] = "."

                for element in burrows:
                    if element != player:
                        player = element

                matrix[player[0]][player[1]] = "S"

        else:
            matrix[player[0]][player[1]] = "."
            print("Game over!")
            break

    elif command == "down":

        if 0 <= player[0] + 1 < len(matrix):
            matrix[player[0]][player[1]] = "."
            next_element = matrix[player[0] + 1][player[1]]
            player[0] += 1

            if next_element == "-":
                matrix[player[0]][player[1]] = "S"

            elif next_element == "*":
                matrix[player[0]][player[1]] = "S"
                food += 1
                if food >= 10:
                    print("You won! You fed the snake.")
                    break

            elif next_element == "B":
                matrix[player[0]][player[1]] = "."

                for element in burrows:
                    if element != player:
                        player = element

                matrix[player[0]][player[1]] = "S"

        else:
            matrix[player[0]][player[1]] = "."
            print("Game over!")
            break

    command = input()

print(f"Food eaten: {food}")
for element in matrix:
    print(''.join(element))