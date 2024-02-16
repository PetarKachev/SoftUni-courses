rows = int(input())
car = input()
matrix = []
player = [0, 0]
tunnels = []
kilometers = 0

for row in range(rows):
    data = input().split(" ")
    matrix.append(data)

    for index in range(len(data)):
        if data[index] == "T":
            tunnels.append([row, index])
command = input()

while command != "End":

    if command == "right":
        matrix[player[0]][player[1]] = "."
        player[1] += 1
        next_element = matrix[player[0]][player[1]]

        if next_element == ".":
            kilometers += 10

        elif next_element == "T":
            matrix[player[0]][player[1]] = "."
            kilometers += 30
            for element in tunnels:
                if element != player:
                    player = element
            matrix[player[0]][player[1]] = "."

        elif next_element == "F":
            kilometers += 10
            matrix[player[0]][player[1]] = "C"
            print(f"Racing car {car} finished the stage!")
            print(f"Distance covered {kilometers} km.")
            for element in matrix:
                print("".join(element))
            exit()

    elif command == "left":
        matrix[player[0]][player[1]] = "."
        player[1] -= 1
        next_element = matrix[player[0]][player[1]]

        if next_element == ".":
            kilometers += 10

        elif next_element == "T":
            matrix[player[0]][player[1]] = "."
            kilometers += 30
            for element in tunnels:
                if element != player:
                    player = element
            matrix[player[0]][player[1]] = "."

        elif next_element == "F":
            kilometers += 10
            matrix[player[0]][player[1]] = "C"
            print(f"Racing car {car} finished the stage!")
            print(f"Distance covered {kilometers} km.")
            for element in matrix:
                print("".join(element))
            exit()

    elif command == "up":
        matrix[player[0]][player[1]] = "."
        player[0] -= 1
        next_element = matrix[player[0]][player[1]]

        if next_element == ".":
            kilometers += 10

        elif next_element == "T":
            matrix[player[0]][player[1]] = "."
            kilometers += 30
            for element in tunnels:
                if element != player:
                    player = element
            matrix[player[0]][player[1]] = "."

        elif next_element == "F":
            kilometers += 10
            matrix[player[0]][player[1]] = "C"
            print(f"Racing car {car} finished the stage!")
            print(f"Distance covered {kilometers} km.")
            for element in matrix:
                print("".join(element))
            exit()

    elif command == "down":
        matrix[player[0]][player[1]] = "."
        player[0] += 1
        next_element = matrix[player[0]][player[1]]

        if next_element == ".":
            kilometers += 10

        elif next_element == "T":
            matrix[player[0]][player[1]] = "."
            kilometers += 30
            for element in tunnels:
                if element != player:
                    player = element
            matrix[player[0]][player[1]] = "."

        elif next_element == "F":
            kilometers += 10
            matrix[player[0]][player[1]] = "C"
            print(f"Racing car {car} finished the stage!")
            print(f"Distance covered {kilometers} km.")
            for element in matrix:
                print("".join(element))
            exit()

    command = input()

matrix[player[0]][player[1]] = "C"
print(f"Racing car {car} DNF.")
print(f"Distance covered {kilometers} km.")
for element in matrix:
    print("".join(element))
exit()