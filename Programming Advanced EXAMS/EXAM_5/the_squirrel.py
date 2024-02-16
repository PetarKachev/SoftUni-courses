hazelnuts = 0
rows = int(input())
moves = input().split(', ')
matrix = []
player = []
for row in range(rows):
    data = list(input())
    matrix.append(data)
    for element in range(len(data)):
        if data[element] == "s":
            player.append(row)
            player.append(element)

for move in moves:

    if move == "up":
        if 0 <= player[0] - 1 < rows:

            if matrix[player[0] - 1][player[1]] == "*":
                matrix[player[0]][player[1]] = "*"
                player[0] -= 1
                matrix[player[0]][player[1]] = "s"

            elif matrix[player[0] - 1][player[1]] == "h":
                matrix[player[0]][player[1]] = "*"
                player[0] -= 1
                matrix[player[0]][player[1]] = "s"
                hazelnuts += 1
                if hazelnuts == 3:
                    print("Good job! You have collected all hazelnuts!")
                    print(f"Hazelnuts collected: {hazelnuts}")
                    exit()

            elif matrix[player[0] - 1][player[1]] == "t":
                matrix[player[0]][player[1]] = "*"
                player[0] -= 1
                matrix[player[0]][player[1]] = "s"
                print("Unfortunately, the squirrel stepped on a trap...")
                print(f"Hazelnuts collected: {hazelnuts}")
                exit()
        else:
            print("The squirrel is out of the field.")
            print(f"Hazelnuts collected: {hazelnuts}")
            exit()

    elif move == "down":
        if 0 <= player[0] + 1 < rows:

            if matrix[player[0] + 1][player[1]] == "*":
                matrix[player[0]][player[1]] = "*"
                player[0] += 1
                matrix[player[0]][player[1]] = "s"

            elif matrix[player[0] + 1][player[1]] == "h":
                matrix[player[0]][player[1]] = "*"
                player[0] += 1
                matrix[player[0]][player[1]] = "s"
                hazelnuts += 1
                if hazelnuts == 3:
                    print("Good job! You have collected all hazelnuts!")
                    print(f"Hazelnuts collected: {hazelnuts}")
                    exit()

            elif matrix[player[0] + 1][player[1]] == "t":
                matrix[player[0]][player[1]] = "*"
                player[0] += 1
                matrix[player[0]][player[1]] = "s"
                print("Unfortunately, the squirrel stepped on a trap...")
                print(f"Hazelnuts collected: {hazelnuts}")
                exit()
        else:
            print("The squirrel is out of the field.")
            print(f"Hazelnuts collected: {hazelnuts}")
            exit()

    elif move == "right":
        if 0 <= player[1] + 1 < rows:

            if matrix[player[0]][player[1] + 1] == "*":
                matrix[player[0]][player[1]] = "*"
                player[1] += 1
                matrix[player[0]][player[1]] = "s"

            elif matrix[player[0]][player[1] + 1] == "h":
                matrix[player[0]][player[1]] = "*"
                player[1] += 1
                matrix[player[0]][player[1]] = "s"
                hazelnuts += 1
                if hazelnuts == 3:
                    print("Good job! You have collected all hazelnuts!")
                    print(f"Hazelnuts collected: {hazelnuts}")
                    exit()

            elif matrix[player[0]][player[1] + 1] == "t":
                matrix[player[0]][player[1]] = "*"
                player[1] += 1
                matrix[player[0]][player[1]] = "s"
                print("Unfortunately, the squirrel stepped on a trap...")
                print(f"Hazelnuts collected: {hazelnuts}")
                exit()
        else:
            print("The squirrel is out of the field.")
            print(f"Hazelnuts collected: {hazelnuts}")
            exit()

    elif move == "left":
        if 0 <= player[1] - 1 < rows:

            if matrix[player[0]][player[1] - 1] == "*":
                matrix[player[0]][player[1]] = "*"
                player[1] -= 1
                matrix[player[0]][player[1]] = "s"

            elif matrix[player[0]][player[1] - 1] == "h":
                matrix[player[0]][player[1]] = "*"
                player[1] -= 1
                matrix[player[0]][player[1]] = "s"
                hazelnuts += 1
                if hazelnuts == 3:
                    print("Good job! You have collected all hazelnuts!")
                    print(f"Hazelnuts collected: {hazelnuts}")
                    exit()

            elif matrix[player[0]][player[1] - 1] == "t":
                matrix[player[0]][player[1]] = "*"
                player[1] -= 1
                matrix[player[0]][player[1]] = "s"
                print("Unfortunately, the squirrel stepped on a trap...")
                print(f"Hazelnuts collected: {hazelnuts}")
                exit()
        else:
            print("The squirrel is out of the field.")
            print(f"Hazelnuts collected: {hazelnuts}")
            exit()

print("There are more hazelnuts to collect.")
print(f"Hazelnuts collected: {hazelnuts}")