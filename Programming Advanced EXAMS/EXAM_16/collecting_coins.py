rows = int(input())
matrix = []
player = []
path = []
coins = 0

for row in range(rows):
    data = input().split(" ")
    matrix.append(data)
    for index in range(len(data)):
        if data[index] == "P":
            player.append(row)
            player.append(index)
            path.append([row, index])

command = input()
while command:

    if command == 'up':

        matrix[player[0]][player[1]] = "."

        if 0 <= player[0] - 1 < rows:

            next_element = matrix[player[0] - 1][player[1]]
            player[0] -= 1

            if next_element == ".":
                path.append([player[0], player[1]])

            elif str(next_element).isdigit():
                path.append([player[0], player[1]])
                coins += int(matrix[player[0]][player[1]])
                if coins >= 100:
                    print(f"You won! You've collected {round(coins)} coins.")
                    print("Your path:")
                    for element in path:
                        print(element)
                    exit()

            elif next_element == "X":
                path.append([player[0], player[1]])
                print(f"Game over! You've collected {round(coins / 2)} coins.")
                break

        else:
            player[0] = rows - 1
            next_element = matrix[player[0]][player[1]]

            if next_element == ".":
                path.append([player[0], player[1]])

            elif str(next_element).isdigit():
                path.append([player[0], player[1]])
                coins += int(matrix[player[0]][player[1]])
                if coins >= 100:
                    print(f"You won! You've collected {round(coins)} coins.")
                    print("Your path:")
                    for element in path:
                        print(element)
                    exit()

            elif next_element == "X":
                path.append([player[0], player[1]])
                print(f"Game over! You've collected {round(coins / 2)} coins.")
                break

    elif command == "down":

        matrix[player[0]][player[1]] = "."

        if 0 <= player[0] + 1 < rows:

            next_element = matrix[player[0] + 1][player[1]]
            player[0] += 1

            if next_element == ".":
                path.append([player[0], player[1]])

            elif str(next_element).isdigit():
                path.append([player[0], player[1]])
                coins += int(matrix[player[0]][player[1]])
                if coins >= 100:
                    print(f"You won! You've collected {round(coins)} coins.")
                    print("Your path:")
                    for element in path:
                        print(element)
                    exit()

            elif next_element == "X":
                path.append([player[0], player[1]])
                print(f"Game over! You've collected {round(coins / 2)} coins.")
                break

        else:
            player[0] = 0
            next_element = matrix[player[0]][player[1]]

            if next_element == ".":
                path.append([player[0], player[1]])

            elif str(next_element).isdigit():
                path.append([player[0], player[1]])
                coins += int(matrix[player[0]][player[1]])
                if coins >= 100:
                    print(f"You won! You've collected {round(coins)} coins.")
                    print("Your path:")
                    for element in path:
                        print(element)
                    exit()

            elif next_element == "X":
                path.append([player[0], player[1]])
                print(f"Game over! You've collected {round(coins / 2)} coins.")
                break

    elif command == "right":

        matrix[player[0]][player[1]] = "."

        if 0 <= player[1] + 1 < rows:

            next_element = matrix[player[0]][player[1] + 1]
            player[1] += 1

            if next_element == ".":
                path.append([player[0], player[1]])

            elif str(next_element).isdigit():
                path.append([player[0], player[1]])
                coins += int(matrix[player[0]][player[1]])
                if coins >= 100:
                    print(f"You won! You've collected {round(coins)} coins.")
                    print("Your path:")
                    for element in path:
                        print(element)
                    exit()

            elif next_element == "X":
                path.append([player[0], player[1]])
                print(f"Game over! You've collected {round(coins / 2)} coins.")
                break

        else:
            player[1] = 0
            next_element = matrix[player[0]][player[1]]

            if next_element == ".":
                path.append([player[0], player[1]])

            elif str(next_element).isdigit():
                path.append([player[0], player[1]])
                coins += int(matrix[player[0]][player[1]])
                if coins >= 100:
                    print(f"You won! You've collected {round(coins)} coins.")
                    print("Your path:")
                    for element in path:
                        print(element)
                    exit()

            elif next_element == "X":
                path.append([player[0], player[1]])
                print(f"Game over! You've collected {round(coins / 2)} coins.")
                break

    elif command == "left":

        matrix[player[0]][player[1]] = "."

        if 0 <= player[1] - 1 < rows:

            next_element = matrix[player[0]][player[1] - 1]
            player[1] -= 1

            if next_element == ".":
                path.append([player[0], player[1]])

            elif str(next_element).isdigit():
                path.append([player[0], player[1]])
                coins += int(matrix[player[0]][player[1]])
                if coins >= 100:
                    print(f"You won! You've collected {round(coins)} coins.")
                    print("Your path:")
                    for element in path:
                        print(element)
                    exit()

            elif next_element == "X":
                path.append([player[0], player[1]])
                print(f"Game over! You've collected {round(coins / 2)} coins.")
                break

        else:
            player[1] = rows - 1
            next_element = matrix[player[0]][player[1]]

            if next_element == ".":
                path.append([player[0], player[1]])

            elif str(next_element).isdigit():
                path.append([player[0], player[1]])
                coins += int(matrix[player[0]][player[1]])
                if coins >= 100:
                    print(f"You won! You've collected {round(coins)} coins.")
                    print("Your path:")
                    for element in path:
                        print(element)
                    exit()

            elif next_element == "X":
                path.append([player[0], player[1]])
                print(f"Game over! You've collected {round(coins / 2)} coins.")
                break

    command = input()

print("Your path:")
for element in path:
    print(element)
exit()