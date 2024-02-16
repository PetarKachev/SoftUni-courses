rows = int(input())
matrix = []
alice_pos = []
collected_bags = 0

for row in range(rows):
    data = list(map(str, input().split(" ")))
    matrix.append(data)
    for element in data:
        if element == "A":
            needed_index = data.index(element)
            alice_pos.append(row)
            alice_pos.append(needed_index)
command = input()
len_columns = len(matrix[0])

while command:
    if command == "up":

        if 0 <= alice_pos[0] - 1 < rows:
            matrix[alice_pos[0]][alice_pos[1]] = "*"
            if matrix[alice_pos[0] - 1][alice_pos[1]] == ".":
                matrix[alice_pos[0] - 1][alice_pos[1]] = "A"
                alice_pos[0] -= 1

            elif matrix[alice_pos[0] - 1][alice_pos[1]] == "*":
                matrix[alice_pos[0] - 1][alice_pos[1]] = "A"
                alice_pos[0] -= 1

            elif matrix[alice_pos[0] - 1][alice_pos[1]].isdigit():
                collected_bags += int(matrix[alice_pos[0] - 1][alice_pos[1]])
                if collected_bags >= 10:
                    matrix[alice_pos[0] - 1][alice_pos[1]] = "*"
                    print("She did it! She went to the party.")
                    for element in matrix:
                        print(' '.join(element))
                    exit()
                matrix[alice_pos[0] - 1][alice_pos[1]] = "A"
                alice_pos[0] -= 1

            elif matrix[alice_pos[0] - 1][alice_pos[1]] == "R":
                matrix[alice_pos[0] - 1][alice_pos[1]] = "*"
                print("Alice didn't make it to the tea party.")
                for element in matrix:
                    print(' '.join(element))
                exit()
        else:
            matrix[alice_pos[0]][alice_pos[1]] = "*"
            print("Alice didn't make it to the tea party.")
            for element in matrix:
                print(' '.join(element))
            exit()

    elif command == "down":
        if 0 <= alice_pos[0] + 1 < rows:
            matrix[alice_pos[0]][alice_pos[1]] = "*"
            if matrix[alice_pos[0] + 1][alice_pos[1]] == ".":
                matrix[alice_pos[0] + 1][alice_pos[1]] = "A"
                alice_pos[0] += 1

            elif matrix[alice_pos[0] + 1][alice_pos[1]] == "*":
                matrix[alice_pos[0] + 1][alice_pos[1]] = "A"
                alice_pos[0] += 1

            elif matrix[alice_pos[0] + 1][alice_pos[1]].isdigit():
                collected_bags += int(matrix[alice_pos[0] + 1][alice_pos[1]])
                if collected_bags >= 10:
                    matrix[alice_pos[0] + 1][alice_pos[1]] = "*"
                    print("She did it! She went to the party.")
                    for element in matrix:
                        print(' '.join(element))
                    exit()
                matrix[alice_pos[0] + 1][alice_pos[1]] = "A"
                alice_pos[0] += 1

            elif matrix[alice_pos[0] + 1][alice_pos[1]] == "R":
                matrix[alice_pos[0] + 1][alice_pos[1]] = "*"
                print("Alice didn't make it to the tea party.")
                for element in matrix:
                    print(' '.join(element))
                exit()
        else:
            matrix[alice_pos[0]][alice_pos[1]] = "*"
            print("Alice didn't make it to the tea party.")
            for element in matrix:
                print(' '.join(element))
            exit()

    elif command == "left":
        if 0 <= alice_pos[1] - 1 < len_columns:
            matrix[alice_pos[0]][alice_pos[1]] = "*"
            if matrix[alice_pos[0]][alice_pos[1] - 1] == ".":
                matrix[alice_pos[0]][alice_pos[1] - 1] = "A"
                alice_pos[1] -= 1

            elif matrix[alice_pos[0]][alice_pos[1] - 1] == "*":
                matrix[alice_pos[0]][alice_pos[1] - 1] = "A"
                alice_pos[1] -= 1

            elif matrix[alice_pos[0]][alice_pos[1] - 1].isdigit():
                collected_bags += int(matrix[alice_pos[0]][alice_pos[1] - 1])
                if collected_bags >= 10:
                    matrix[alice_pos[0]][alice_pos[1] - 1] = "*"
                    print("She did it! She went to the party.")
                    for element in matrix:
                        print(' '.join(element))
                    exit()
                matrix[alice_pos[0]][alice_pos[1] - 1] = "A"
                alice_pos[1] -= 1

            elif matrix[alice_pos[0]][alice_pos[1] - 1] == "R":
                matrix[alice_pos[0]][alice_pos[1] - 1] = "*"
                print("Alice didn't make it to the tea party.")
                for element in matrix:
                    print(' '.join(element))
                exit()

        else:
            matrix[alice_pos[0]][alice_pos[1]] = "*"
            print("Alice didn't make it to the tea party.")
            for element in matrix:
                print(' '.join(element))
            exit()

    elif command == "right":
        if 0 <= alice_pos[1] + 1 < len_columns:
            matrix[alice_pos[0]][alice_pos[1]] = "*"
            if matrix[alice_pos[0]][alice_pos[1] + 1] == ".":
                matrix[alice_pos[0]][alice_pos[1] + 1] = "A"
                alice_pos[1] += 1

            if matrix[alice_pos[0]][alice_pos[1] + 1] == "*":
                matrix[alice_pos[0]][alice_pos[1] + 1] = "A"
                alice_pos[1] += 1

            elif matrix[alice_pos[0]][alice_pos[1] + 1].isdigit():
                collected_bags += int(matrix[alice_pos[0]][alice_pos[1] + 1])
                if collected_bags >= 10:
                    matrix[alice_pos[0]][alice_pos[1] + 1] = "*"
                    print("She did it! She went to the party.")
                    for element in matrix:
                        print(' '.join(element))
                    exit()
                matrix[alice_pos[0]][alice_pos[1] + 1] = "A"
                alice_pos[1] += 1

            elif matrix[alice_pos[0]][alice_pos[1] + 1] == "R":
                matrix[alice_pos[0]][alice_pos[1] + 1] = "*"
                print("Alice didn't make it to the tea party.")
                for element in matrix:
                    print(' '.join(element))
                exit()
        else:
            matrix[alice_pos[0]][alice_pos[1]] = "*"
            print("Alice didn't make it to the tea party.")
            for element in matrix:
                print(' '.join(element))
            exit()
    command = input()