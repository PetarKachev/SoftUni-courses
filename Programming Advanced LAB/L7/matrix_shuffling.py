info = list(map(int, input().split(" ")))
rows = info[0]
columns = info[1]
matrix = []

for row in range(rows):
    data = input().split(" ")
    matrix.append(data)

command = input()
while command != "END":
    command = command.split(" ")
    if len(command) == 5:
        if command[0] == "swap" and command[1].isdigit() > 0 and command[2].isdigit() > 0 and command[3].isdigit() > 0 and command[4].isdigit() > 0:
            if int(command[1]) < len(matrix[0]) and int(command[2]) < len(matrix[0]) and int(command[3]) < len(matrix[0]) and int(command[4]) < len(matrix[0]):
                first_num = int(command[1])
                second_num = int(command[2])
                third_num = int(command[3])
                forth_num = int(command[4])
                for row in range(rows):
                    for col in range(columns):
                        first_symbol = matrix[first_num][second_num]
                        second_symbol = matrix[third_num][forth_num]
                        matrix[first_num][second_num] = second_symbol
                        matrix[third_num][forth_num] = first_symbol

                        for element in matrix:
                            print(' '.join(element))
                        break
                    break
            else:
                print("Invalid input!")
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")


    command = input()