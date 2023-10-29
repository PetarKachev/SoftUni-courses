width = int(input())
length = int(input())
height = int(input())
free_space = width * length * height

data = input()
while data != 'Done':
    boxes = int(data)
    free_space -= boxes

    if free_space <= 0:
        break

    data = input()

diff = abs(free_space)
if data == 'Done':
    print(f"{diff} Cubic meters left.")
if free_space <= 0:
    print(f"No more free space! You need {diff} Cubic meters more.")