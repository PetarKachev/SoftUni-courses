from collections import deque
queue = deque()
water_quantity = int(input())

name = input()

while name != "Start":
    queue.append(name)
    name = input()

command = input()
while command != "End":
    if "refill" in command:
        command = command.split(" ")
        water_quantity += int(command[1])
    else:
        liters = int(command)
        if liters <= water_quantity:
            water_quantity -= liters
            print(f"{queue.popleft()} got water")
        else:
            print(f"{queue.popleft()} must wait")
    command = input()

print(f"{water_quantity} liters left")