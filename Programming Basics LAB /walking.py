sum_steps = 0
goal = 10000

data = input()
while data != 'Going home':
    steps = int(data)
    sum_steps += steps

    if sum_steps >= goal:
        break

    data = input()

if data == 'Going home':
    steps_home = int(input())
    sum_steps += steps_home

diff = abs(sum_steps - goal)
if sum_steps >= goal:
    print(f"Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")
