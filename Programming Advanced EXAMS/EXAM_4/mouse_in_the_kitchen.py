info = list(map(int, input().split(",")))
rows = int(info[0])
cols = int(info[1])
mouse_pos = []
matrix = []
number_of_cheeses = 0
for row in range(rows):
    data = list(input())
    matrix.append(data)
    for index in range(len(data)):
        if data[index] == "M":
            mouse_pos.append(row)
            mouse_pos.append(index)
        elif data[index] == "C":
            number_of_cheeses += 1

command = input()
while command != "danger":
    if command == "up":
        if 0 <= mouse_pos[0] - 1 < rows:
            if matrix[mouse_pos[0] - 1][mouse_pos[1]] != "@":
                if matrix[mouse_pos[0] - 1][mouse_pos[1]] == "*":
                    matrix[mouse_pos[0]][mouse_pos[1]] = "*"
                    mouse_pos[0] -= 1
                    matrix[mouse_pos[0]][mouse_pos[1]] = "M"

                elif matrix[mouse_pos[0] - 1][mouse_pos[1]] == "C":
                    matrix[mouse_pos[0]][mouse_pos[1]] = "*"
                    mouse_pos[0] -= 1
                    matrix[mouse_pos[0]][mouse_pos[1]] = "M"
                    number_of_cheeses -= 1
                    if number_of_cheeses == 0:
                        print("Happy mouse! All the cheese is eaten, good night!")
                        for element in matrix:
                            print(''.join(element))
                        exit()

                elif matrix[mouse_pos[0] - 1][mouse_pos[1]] == "T":
                    matrix[mouse_pos[0]][mouse_pos[1]] = "*"
                    mouse_pos[0] -= 1
                    matrix[mouse_pos[0]][mouse_pos[1]] = "M"
                    print("Mouse is trapped!")
                    for element in matrix:
                        print(''.join(element))
                    exit()
        else:
            print("No more cheese for tonight!")
            for element in matrix:
                print(''.join(element))
            exit()

    elif command == "down":
        if 0 <= mouse_pos[0] + 1 < rows:
            if matrix[mouse_pos[0] + 1][mouse_pos[1]] != "@":
                if matrix[mouse_pos[0] + 1][mouse_pos[1]] == "*":
                    matrix[mouse_pos[0]][mouse_pos[1]] = "*"
                    mouse_pos[0] += 1
                    matrix[mouse_pos[0]][mouse_pos[1]] = "M"

                elif matrix[mouse_pos[0] + 1][mouse_pos[1]] == "C":
                    matrix[mouse_pos[0]][mouse_pos[1]] = "*"
                    mouse_pos[0] += 1
                    matrix[mouse_pos[0]][mouse_pos[1]] = "M"
                    number_of_cheeses -= 1
                    if number_of_cheeses == 0:
                        print("Happy mouse! All the cheese is eaten, good night!")
                        for element in matrix:
                            print(''.join(element))
                        exit()

                elif matrix[mouse_pos[0] + 1][mouse_pos[1]] == "T":
                    matrix[mouse_pos[0]][mouse_pos[1]] = "*"
                    mouse_pos[0] += 1
                    matrix[mouse_pos[0]][mouse_pos[1]] = "M"
                    print("Mouse is trapped!")
                    for element in matrix:
                        print(''.join(element))
                    exit()
        else:
            print("No more cheese for tonight!")
            for element in matrix:
                print(''.join(element))
            exit()

    elif command == "right":
        if 0 <= mouse_pos[1] + 1 < cols:
            if matrix[mouse_pos[0]][mouse_pos[1] + 1] != "@":
                if matrix[mouse_pos[0]][mouse_pos[1] + 1] == "*":
                    matrix[mouse_pos[0]][mouse_pos[1]] = "*"
                    mouse_pos[1] += 1
                    matrix[mouse_pos[0]][mouse_pos[1]] = "M"

                elif matrix[mouse_pos[0]][mouse_pos[1] + 1] == "C":
                    matrix[mouse_pos[0]][mouse_pos[1]] = "*"
                    mouse_pos[1] += 1
                    matrix[mouse_pos[0]][mouse_pos[1]] = "M"
                    number_of_cheeses -= 1
                    if number_of_cheeses == 0:
                        print("Happy mouse! All the cheese is eaten, good night!")
                        for element in matrix:
                            print(''.join(element))
                        exit()

                elif matrix[mouse_pos[0]][mouse_pos[1] + 1] == "T":
                    matrix[mouse_pos[0]][mouse_pos[1]] = "*"
                    mouse_pos[1] += 1
                    matrix[mouse_pos[0]][mouse_pos[1]] = "M"
                    print("Mouse is trapped!")
                    for element in matrix:
                        print(''.join(element))
                    exit()
        else:
            print("No more cheese for tonight!")
            for element in matrix:
                print(''.join(element))
            exit()

    elif command == "left":
        if 0 <= mouse_pos[1] - 1 < cols:
            if matrix[mouse_pos[0]][mouse_pos[1] - 1] != "@":
                if matrix[mouse_pos[0]][mouse_pos[1] - 1] == "*":
                    matrix[mouse_pos[0]][mouse_pos[1]] = "*"
                    mouse_pos[1] -= 1
                    matrix[mouse_pos[0]][mouse_pos[1]] = "M"

                elif matrix[mouse_pos[0]][mouse_pos[1] - 1] == "C":
                    matrix[mouse_pos[0]][mouse_pos[1]] = "*"
                    mouse_pos[1] -= 1
                    matrix[mouse_pos[0]][mouse_pos[1]] = "M"
                    number_of_cheeses -= 1
                    if number_of_cheeses == 0:
                        print("Happy mouse! All the cheese is eaten, good night!")
                        for element in matrix:
                            print(''.join(element))
                        exit()

                elif matrix[mouse_pos[0]][mouse_pos[1] - 1] == "T":
                    matrix[mouse_pos[0]][mouse_pos[1]] = "*"
                    mouse_pos[1] -= 1
                    matrix[mouse_pos[0]][mouse_pos[1]] = "M"
                    print("Mouse is trapped!")
                    for element in matrix:
                        print(''.join(element))
                    exit()
        else:
            print("No more cheese for tonight!")
            for element in matrix:
                print(''.join(element))
            exit()
    command = input()

if number_of_cheeses > 0:
    print("Mouse will come back later!")
    for element in matrix:
        print(''.join(element))