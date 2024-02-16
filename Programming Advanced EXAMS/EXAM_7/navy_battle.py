rows = int(input())
cols = rows
matrix = []
submarine = []
destroyed_cruisers = 0
taken_damages = 0
for row in range(rows):
    data = list(input())
    matrix.append(data)
    for element in range(len(data)):
        if data[element] == "S":
            submarine.append(row)
            submarine.append(element)

command = input()
while command:
    if command == "up":
        if 0 <= submarine[0] - 1 < rows:

            if matrix[submarine[0] - 1][submarine[1]] == "-":
                matrix[submarine[0]][submarine[1]] = "-"
                submarine[0] -= 1
                matrix[submarine[0]][submarine[1]] = "S"
            elif matrix[submarine[0] - 1][submarine[1]] == "*":
                matrix[submarine[0]][submarine[1]] = "-"
                submarine[0] -= 1
                matrix[submarine[0]][submarine[1]] = "S"
                taken_damages += 1
                if taken_damages == 3:
                    print(f"Mission failed, U-9 disappeared! Last known coordinates [{submarine[0]}, {submarine[1]}]!")
                    break
            elif matrix[submarine[0] - 1][submarine[1]] == "C":
                matrix[submarine[0]][submarine[1]] = "-"
                submarine[0] -= 1
                matrix[submarine[0]][submarine[1]] = "S"
                destroyed_cruisers += 1
                if destroyed_cruisers == 3:
                    print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
                    break

    elif command == "down":
        if 0 <= submarine[0] + 1 < rows:

            if matrix[submarine[0] + 1][submarine[1]] == "-":
                matrix[submarine[0]][submarine[1]] = "-"
                submarine[0] += 1
                matrix[submarine[0]][submarine[1]] = "S"
            elif matrix[submarine[0] + 1][submarine[1]] == "*":
                matrix[submarine[0]][submarine[1]] = "-"
                submarine[0] += 1
                matrix[submarine[0]][submarine[1]] = "S"
                taken_damages += 1
                if taken_damages == 3:
                    print(f"Mission failed, U-9 disappeared! Last known coordinates [{submarine[0]}, {submarine[1]}]!")
                    break
            elif matrix[submarine[0] + 1][submarine[1]] == "C":
                matrix[submarine[0]][submarine[1]] = "-"
                submarine[0] += 1
                matrix[submarine[0]][submarine[1]] = "S"
                destroyed_cruisers += 1
                if destroyed_cruisers == 3:
                    print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
                    break

    elif command == "right":
        if 0 <= submarine[1] + 1 < cols:

            if matrix[submarine[0]][submarine[1] + 1] == "-":
                matrix[submarine[0]][submarine[1]] = "-"
                submarine[1] += 1
                matrix[submarine[0]][submarine[1]] = "S"
            elif matrix[submarine[0]][submarine[1] + 1] == "*":
                matrix[submarine[0]][submarine[1]] = "-"
                submarine[1] += 1
                matrix[submarine[0]][submarine[1]] = "S"
                taken_damages += 1
                if taken_damages == 3:
                    print(f"Mission failed, U-9 disappeared! Last known coordinates [{submarine[0]}, {submarine[1]}]!")
                    break
            elif matrix[submarine[0]][submarine[1] + 1] == "C":
                matrix[submarine[0]][submarine[1]] = "-"
                submarine[1] += 1
                matrix[submarine[0]][submarine[1]] = "S"
                destroyed_cruisers += 1
                if destroyed_cruisers == 3:
                    print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
                    break

    elif command == "left":
        if 0 <= submarine[1] - 1 < cols:

            if matrix[submarine[0]][submarine[1] - 1] == "-":
                matrix[submarine[0]][submarine[1]] = "-"
                submarine[1] -= 1
                matrix[submarine[0]][submarine[1]] = "S"
            elif matrix[submarine[0]][submarine[1] - 1] == "*":
                matrix[submarine[0]][submarine[1]] = "-"
                submarine[1] -= 1
                matrix[submarine[0]][submarine[1]] = "S"
                taken_damages += 1
                if taken_damages == 3:
                    print(f"Mission failed, U-9 disappeared! Last known coordinates [{submarine[0]}, {submarine[1]}]!")
                    break
            elif matrix[submarine[0]][submarine[1] - 1] == "C":
                matrix[submarine[0]][submarine[1]] = "-"
                submarine[1] -= 1
                matrix[submarine[0]][submarine[1]] = "S"
                destroyed_cruisers += 1
                if destroyed_cruisers == 3:
                    print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
                    break
    command = input()

for element in matrix:
    print(''.join(element))