from collections import deque
eggs = deque(list(map(int, input().split(", "))))
paper = deque(list(map(int, input().split(", "))))
filled_boxes = 0

while eggs and paper:
    if eggs[0] <= 0:
        eggs.popleft()
    elif eggs[0] == 13:
        eggs.popleft()
        first_pos = paper.popleft()
        last_pos = paper.pop()
        paper.insert(0, last_pos)
        paper.append(first_pos)
    else:
        if eggs[0] + paper[-1] <= 50:
            filled_boxes += 1
            eggs.popleft()
            paper.pop()
        else:
            eggs.popleft()
            paper.pop()

if filled_boxes >= 1:
    print(f"Great! You filled {filled_boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")
if eggs:
    print(f"Eggs left: {', '.join(str(el) for el in eggs)}")
if paper:
    print(f"Pieces of paper left: {', '.join(str(el) for el in paper)}")