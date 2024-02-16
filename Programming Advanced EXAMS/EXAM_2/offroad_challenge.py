from collections import deque
fuel = deque(list(map(int, input().split(" "))))
consump_index = deque(list(map(int, input().split(" "))))
needed_fuel = deque(list(map(int, input().split(" "))))
the_top = len(needed_fuel)
reached_altitude = 0
list_with_altitudes = []

while fuel and consump_index:
    if fuel[-1] - consump_index[0] >= needed_fuel[0]:
        reached_altitude += 1
        list_with_altitudes.append(f'Altitude {reached_altitude}')
        fuel.pop()
        consump_index.popleft()
        needed_fuel.popleft()
        print(f"John has reached: Altitude {reached_altitude}")
    else:
        print(f"John did not reach: Altitude {reached_altitude + 1}")
        break

if reached_altitude == the_top:
    print("John has reached all the altitudes and managed to reach the top!")
elif reached_altitude == 0:
    print("John failed to reach the top.")
    print("John didn't reach any altitude.")
else:
    print("John failed to reach the top.")
    print(f"Reached altitudes: {', '.join(list_with_altitudes)}")