matrix = []
rows = 6
cols = 6
player = []
water_deposit = 0
metal_deposit = 0
concrete_deposit = 0
for row in range(rows):
    data = input().split(" ")
    matrix.append(data)
    for index in range(len(data)):
        if data[index] == "E":
            player.append(row)
            player.append(index)
moves = input().split(", ")

for move in moves:
    if move == "up":

        if 0 <= player[0] - 1 < rows:
            if matrix[player[0] - 1][player[1]] == "-":
                player[0] -= 1
            elif matrix[player[0] - 1][player[1]] == "W":
                player[0] -= 1
                print(f"Water deposit found at ({player[0]}, {player[1]})")
                water_deposit += 1
            elif matrix[player[0] - 1][player[1]] == "M":
                player[0] -= 1
                print(f"Metal deposit found at ({player[0]}, {player[1]})")
                metal_deposit += 1
            elif matrix[player[0] - 1][player[1]] == "C":
                player[0] -= 1
                print(f"Concrete deposit found at ({player[0]}, {player[1]})")
                concrete_deposit += 1
            elif matrix[player[0] - 1][player[1]] == "R":
                player[0] -= 1
                print(f"Rover got broken at ({player[0]}, {player[1]})")
                break
        else:
            if player[0] - 1 < 0:
                player[0] = rows - 1
                if matrix[player[0]][player[1]] == "-":
                    pass
                elif matrix[player[0]][player[1]] == "W":
                    print(f"Water deposit found at ({player[0]}, {player[1]})")
                    water_deposit += 1
                elif matrix[player[0]][player[1]] == "M":
                    print(f"Metal deposit found at ({player[0]}, {player[1]})")
                    metal_deposit += 1
                elif matrix[player[0]][player[1]] == "C":
                    print(f"Concrete deposit found at ({player[0]}, {player[1]})")
                    concrete_deposit += 1
                elif matrix[player[0]][player[1]] == "R":
                    print(f"Rover got broken at ({player[0]}, {player[1]})")
                    break

    elif move == "down":

        if 0 <= player[0] + 1 < rows:
            if matrix[player[0] + 1][player[1]] == "-":
                player[0] += 1
            elif matrix[player[0] + 1][player[1]] == "W":
                player[0] += 1
                print(f"Water deposit found at ({player[0]}, {player[1]})")
                water_deposit += 1
            elif matrix[player[0] + 1][player[1]] == "M":
                player[0] += 1
                print(f"Metal deposit found at ({player[0]}, {player[1]})")
                metal_deposit += 1
            elif matrix[player[0] + 1][player[1]] == "C":
                player[0] += 1
                print(f"Concrete deposit found at ({player[0]}, {player[1]})")
                concrete_deposit += 1
            elif matrix[player[0] + 1][player[1]] == "R":
                player[0] += 1
                print(f"Rover got broken at ({player[0]}, {player[1]})")
                break
        else:
            if player[0] + 1 >= 6:
                player[0] = 0
                if matrix[player[0]][player[1]] == "-":
                    pass
                elif matrix[player[0]][player[1]] == "W":
                    print(f"Water deposit found at ({player[0]}, {player[1]})")
                    water_deposit += 1
                elif matrix[player[0]][player[1]] == "M":
                    print(f"Metal deposit found at ({player[0]}, {player[1]})")
                    metal_deposit += 1
                elif matrix[player[0]][player[1]] == "C":
                    print(f"Concrete deposit found at ({player[0]}, {player[1]})")
                    concrete_deposit += 1
                elif matrix[player[0]][player[1]] == "R":
                    print(f"Rover got broken at ({player[0]}, {player[1]})")
                    break

    elif move == "right":

        if 0 <= player[1] + 1 < cols:
            if matrix[player[0]][player[1] + 1] == "-":
                player[1] += 1
            elif matrix[player[0]][player[1] + 1] == "W":
                player[1] += 1
                print(f"Water deposit found at ({player[0]}, {player[1]})")
                water_deposit += 1
            elif matrix[player[0]][player[1] + 1] == "M":
                player[1] += 1
                print(f"Metal deposit found at ({player[0]}, {player[1]})")
                metal_deposit += 1
            elif matrix[player[0]][player[1] + 1] == "C":
                player[1] += 1
                print(f"Concrete deposit found at ({player[0]}, {player[1]})")
                concrete_deposit += 1
            elif matrix[player[0]][player[1] + 1] == "R":
                player[1] += 1
                print(f"Rover got broken at ({player[0]}, {player[1]})")
                break
        else:
            if player[1] + 1 >= 6:
                player[1] = 0
                if matrix[player[0]][player[1]] == "-":
                    pass
                elif matrix[player[0]][player[1]] == "W":
                    print(f"Water deposit found at ({player[0]}, {player[1]})")
                    water_deposit += 1
                elif matrix[player[0]][player[1]] == "M":
                    print(f"Metal deposit found at ({player[0]}, {player[1]})")
                    metal_deposit += 1
                elif matrix[player[0]][player[1]] == "C":
                    print(f"Concrete deposit found at ({player[0]}, {player[1]})")
                    concrete_deposit += 1
                elif matrix[player[0]][player[1]] == "R":
                    print(f"Rover got broken at ({player[0]}, {player[1]})")
                    break

    elif move == "left":

        if 0 <= player[1] - 1 < cols:
            if matrix[player[0]][player[1] - 1] == "-":
                player[1] -= 1
            elif matrix[player[0]][player[1] - 1] == "W":
                player[1] -= 1
                print(f"Water deposit found at ({player[0]}, {player[1]})")
                water_deposit += 1
            elif matrix[player[0]][player[1] - 1] == "M":
                player[1] -= 1
                print(f"Metal deposit found at ({player[0]}, {player[1]})")
                metal_deposit += 1
            elif matrix[player[0]][player[1] - 1] == "C":
                player[1] -= 1
                print(f"Concrete deposit found at ({player[0]}, {player[1]})")
                concrete_deposit += 1
            elif matrix[player[0]][player[1] - 1] == "R":
                player[1] -= 1
                print(f"Rover got broken at ({player[0]}, {player[1]})")
                break
        else:
            if player[1] - 1 < 0:
                player[1] = cols - 1
                if matrix[player[0]][player[1]] == "-":
                    pass
                elif matrix[player[0]][player[1]] == "W":
                    print(f"Water deposit found at ({player[0]}, {player[1]})")
                    water_deposit += 1
                elif matrix[player[0]][player[1]] == "M":
                    print(f"Metal deposit found at ({player[0]}, {player[1]})")
                    metal_deposit += 1
                elif matrix[player[0]][player[1]] == "C":
                    print(f"Concrete deposit found at ({player[0]}, {player[1]})")
                    concrete_deposit += 1
                elif matrix[player[0]][player[1]] == "R":
                    print(f"Rover got broken at ({player[0]}, {player[1]})")
                    break

if metal_deposit >= 1 and water_deposit >= 1 and concrete_deposit >= 1:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")