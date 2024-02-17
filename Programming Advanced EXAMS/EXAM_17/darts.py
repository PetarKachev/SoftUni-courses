from collections import deque
rows = 7
cols = 7
players = deque(input().split(", "))
scores = {f'{players[0]}': 501, f'{players[1]}': 501}
turns = {f'{players[0]}': 0, f'{players[1]}': 0}
matrix = []

for row in range(rows):
    data = input().split(" ")
    matrix.append(data)

command = input()
while command:
    current_row = int(command[1])
    current_col = int(command[4])
    current_player = players[0]
    turns[current_player] += 1

    if 0 <= current_row < rows and 0 <= current_col < cols:
        current_element = matrix[current_row][current_col]

        if str(current_element).isdigit():
            scores[current_player] -= int(current_element)
            if scores[current_player] <= 0:
                break

        elif current_element == "D":
            first = int(matrix[current_row][0])
            second = int(matrix[current_row][-1])
            third = int(matrix[0][current_col])
            forth = int(matrix[-1][current_col])
            sum_for_deduction = (first + second + third + forth) * 2

            scores[current_player] -= int(sum_for_deduction)
            if scores[current_player] <= 0:
                break

        elif current_element == "T":
            first = int(matrix[current_row][0])
            second = int(matrix[current_row][-1])
            third = int(matrix[0][current_col])
            forth = int(matrix[-1][current_col])
            sum_for_deduction = (first + second + third + forth) * 3

            scores[current_player] -= int(sum_for_deduction)
            if scores[current_player] <= 0:
                break

        elif current_element == "B":
            break

    else:
        pass

    players.rotate(-1)
    command = input()

print(f"{players[0]} won the game with {turns[players[0]]} throws!")