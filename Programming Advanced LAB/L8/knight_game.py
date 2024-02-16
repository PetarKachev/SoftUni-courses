rows = int(input())
matrix = []

for row in range(rows):
    data = list(map(int, input().split(" ")))
    matrix.append(data)
command = input()

while command != "END":
    command = command.split(" ")
    if command[0] == "Add":
        row = int(command[1])
        col = int(command[2])
        value = int(command[3])

        len_rows = len(matrix)
        len_columns = len(matrix[0])

        if row >= 0 and row < len_rows and col >= 0 and col < len_columns:
            matrix[row][col] += value
        else:
            print("Invalid coordinates")

    elif command[0] == "Subtract":
        row = int(command[1])
        col = int(command[2])
        value = int(command[3])

        len_rows = len(matrix)
        len_columns = len(matrix[0])

        if row >= 0 and row < len_rows and col >= 0 and col < len_columns:
            matrix[row][col] -= value
        else:
            print("Invalid coordinates")
    command = input()

for element in matrix:
    print(' '.join(str(el) for el in element))