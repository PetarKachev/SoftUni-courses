from collections import deque
n = int(input())
start_position = 0
stops = 0
pumps = deque()

for _ in range(n):
    current_fuel, distance = input().split(" ")
    pumps.append([int(current_fuel), int(distance)])

while stops < n:
    fuel = 0
    for i in range(n):
        fuel += pumps[i][0]
        distance = pumps[i][1]
        if fuel < distance:
            pumps.rotate(-1)
            start_position += 1
            stops = 0
            break
        fuel -= distance
        stops += 1

print(start_position)