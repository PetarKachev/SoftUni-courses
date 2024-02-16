info = list(map(int, input().split(" ")))
rows = int(info[0])
cols = int(info[1])
matrix = []
player = []
start_position = []
delivered = False
for row in range(rows):
    data = list(input())
    matrix.append(data)
    for element in range(len(data)):
        if data[element] == "B":
            player.append(row)
            player.append(element)
            start_position.append(row)
            start_position.append(element)

command = input()
while command:
    if command == "up":
        if 0 <= player[0] - 1 < rows:
            if matrix[player[0] - 1][player[1]] != "*":
                player[0] -= 1
                if matrix[player[0]][player[1]] == "-":
                    matrix[player[0]][player[1]] = "."
                elif matrix[player[0]][player[1]] == "P":
                    matrix[player[0]][player[1]] = "R"
                    print("Pizza is collected. 10 minutes for delivery.")
                elif matrix[player[0]][player[1]] == "A":
                    matrix[player[0]][player[1]] = "P"
                    print("Pizza is delivered on time! Next order...")
                    break
        else:
            matrix[start_position[0]][start_position[1]] = " "
            print("The delivery is late. Order is canceled.")
            break
    elif command == "down":
        if 0 <= player[0] + 1 < rows:
            if matrix[player[0] + 1][player[1]] != "*":
                player[0] += 1
                if matrix[player[0]][player[1]] == "-":
                    matrix[player[0]][player[1]] = "."
                elif matrix[player[0]][player[1]] == "P":
                    matrix[player[0]][player[1]] = "R"
                    print("Pizza is collected. 10 minutes for delivery.")
                elif matrix[player[0]][player[1]] == "A":
                    matrix[player[0]][player[1]] = "P"
                    print("Pizza is delivered on time! Next order...")
                    break
        else:
            matrix[start_position[0]][start_position[1]] = " "
            print("The delivery is late. Order is canceled.")
            break
    elif command == "right":
        if 0 <= player[1] + 1 < cols:
            if matrix[player[0]][player[1] + 1] != "*":
                player[1] += 1
                if matrix[player[0]][player[1]] == "-":
                    matrix[player[0]][player[1]] = "."
                elif matrix[player[0]][player[1]] == "P":
                    matrix[player[0]][player[1]] = "R"
                    print("Pizza is collected. 10 minutes for delivery.")
                elif matrix[player[0]][player[1]] == "A":
                    matrix[player[0]][player[1]] = "P"
                    print("Pizza is delivered on time! Next order...")
                    break
        else:
            matrix[start_position[0]][start_position[1]] = " "
            print("The delivery is late. Order is canceled.")
            break
    elif command == "left":
        if 0 <= player[1] - 1 < cols:
            if matrix[player[0]][player[1] - 1] != "*":
                player[1] -= 1
                if matrix[player[0]][player[1]] == "-":
                    matrix[player[0]][player[1]] = "."
                elif matrix[player[0]][player[1]] == "P":
                    matrix[player[0]][player[1]] = "R"
                    print("Pizza is collected. 10 minutes for delivery.")
                elif matrix[player[0]][player[1]] == "A":
                    matrix[player[0]][player[1]] = "P"
                    print("Pizza is delivered on time! Next order...")
                    break
        else:
            matrix[start_position[0]][start_position[1]] = " "
            print("The delivery is late. Order is canceled.")
            break
    command = input()

for element in matrix:
    print(''.join(element))