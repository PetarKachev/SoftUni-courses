size = int(input())

QUOTA = 20
matrix = []
sailor_pos = []

caught_fish = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(size):
    matrix.append(list(input()))

    if 'S' in matrix[row]:
        sailor_pos = [row, matrix[row].index('S')]
        matrix[row][sailor_pos[1]] = '-'

command = input()
while command != 'collect the nets':

    new_row = sailor_pos[0] + directions[command][0]
    new_col = sailor_pos[1] + directions[command][1]

    if new_row < 0:
        new_row = size - 1
    elif new_row == size:
        new_row = 0

    if new_col < 0:
        new_col = size - 1
    elif new_col == size:
        new_col = 0

    element = str(matrix[new_row][new_col])
    sailor_pos = [new_row, new_col]
    matrix[new_row][new_col] = '-'

    if element == 'W':
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you "
              f"caught. Last coordinates of the ship: [{','.join(str(x) for x in sailor_pos)}]")
        exit()

    elif element.isdigit():
        caught_fish += int(element)

    command = input()

matrix[sailor_pos[0]][sailor_pos[1]] = 'S'

if caught_fish >= QUOTA:
    print("Success! You managed to reach the quota!")
else:
    diff = QUOTA - caught_fish
    print(f"You didn't catch enough fish and didn't reach the quota! You need {diff} tons of fish more.")

if caught_fish > 0:
    print(f"Amount of fish caught: {caught_fish} tons.")

[print(''.join(row)) for row in matrix]