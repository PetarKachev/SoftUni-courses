from collections import deque
names = deque(input().split(", "))
rows = 6
cols = 6
matrix = []
block_jerry_counter = 0
block_tom_counter = 0

for row in range(rows):
    data = list(map(str, input().split(" ")))
    matrix.append(data)

command = input()
while command:
    row = int(command[1])
    col = int(command[4])
    current_player = names[0]

    if current_player == "Tom":
        if block_tom_counter == 1 or block_tom_counter == 2:
            block_tom_counter += 1
        if block_tom_counter == 0 or block_tom_counter > 2:
            block_tom_counter = 0
            if matrix[row][col] == "E":
                print(f"{current_player} found the Exit and wins the game!")
                exit()
            elif matrix[row][col] == "T":
                print(f"{current_player} is out of the game! The winner is {names[1]}.")
                exit()
            elif matrix[row][col] == "W":
                print(f"{current_player} hits a wall and needs to rest.")
                if current_player == "Tom":
                    block_tom_counter += 1

    elif current_player == "Jerry":
        if block_jerry_counter == 1 or block_jerry_counter == 2:
            block_jerry_counter += 1
        if block_jerry_counter == 0 or block_jerry_counter > 2:
            block_jerry_counter = 0
            if matrix[row][col] == "E":
                print(f"{current_player} found the Exit and wins the game!")
                exit()
            elif matrix[row][col] == "T":
                print(f"{current_player} is out of the game! The winner is {names[1]}.")
                exit()
            elif matrix[row][col] == "W":
                print(f"{current_player} hits a wall and needs to rest.")
                if current_player == "Jerry":
                    block_jerry_counter += 1
    names.append(names.popleft())
    command = input()

