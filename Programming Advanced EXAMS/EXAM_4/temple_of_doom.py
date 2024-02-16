from collections import deque
tools = deque(list(map(int, input().split(" "))))
substances = deque(list(map(int, input().split(" "))))
challenges = list(map(int, input().split(" ")))

while tools and substances:
    if tools[0] * substances[-1] in challenges:
        challenges.remove(tools[0] * substances[-1])
        tools.popleft()
        substances.pop()
    else:
        tools.append(tools.popleft() + 1)
        substances[-1] -= 1
        if substances[-1] <= 0:
            substances.pop()

if len(challenges) > 0:
    print("Harry is lost in the temple. Oblivion awaits him.")
else:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")
if len(tools) > 0:
    print(f"Tools: {', '.join(str(el) for el in tools)}")
if len(substances) > 0:
    print(f"Substances: {', '.join(str(el) for el in substances)}")
if len(challenges) > 0:
    print(f"Challenges: {', '.join(str(el) for el in challenges)}")