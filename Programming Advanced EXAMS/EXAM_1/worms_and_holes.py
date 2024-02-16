from collections import deque
worms = list(map(int, input().split(" ")))
holes = deque(list(map(int, input().split(" "))))
start_number_worms = len(worms)
start_number_holes = len(holes)
matches = 0

while worms and holes:
    if worms[-1] == holes[0]:
        worms.pop()
        holes.popleft()
        matches += 1
    else:
        holes.popleft()
        worms[-1] -= 3
        if worms[-1] <= 0:
            worms.pop()

if matches > 0:
    print(f"Matches: {matches}")
else:
    print("There are no matches.")

if len(worms) == 0 and start_number_worms == matches:
    print("Every worm found a suitable hole!")
elif len(worms) == 0:
    print("Worms left: none")
elif len(worms) > 0:
    print(f"Worms left: {', '.join(str(el) for el in worms)}")

if len(holes) == 0:
    print("Holes left: none")
elif len(holes) > 0:
    print(f"Holes left: {', '.join(str(el) for el in holes)}")