from collections import deque
chocolates = list(map(int, input().split(", ")))
milk_cups = deque(list(map(int, input().split(", "))))
milkshakes = 0

while chocolates and milk_cups and milkshakes < 5:
    if chocolates[-1] <= 0 and milk_cups[0] <= 0:
        chocolates.pop()
        milk_cups.popleft()
        continue
    if chocolates[-1] <= 0:
        chocolates.pop()
        continue
    if milk_cups[0] <= 0:
        milk_cups.popleft()
        continue

    if chocolates[-1] == milk_cups[0]:
        chocolates.pop()
        milk_cups.popleft()
        milkshakes += 1
    else:
        milk_cups.rotate(-1)
        chocolates[-1] -= 5

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if len(chocolates) > 0:
    print(f"Chocolate: {', '.join([str(element) for element in chocolates])}")
else:
    print("Chocolate: empty")

if len(milk_cups) > 0:
    print(f"Milk: {', '.join([str(element) for element in milk_cups])}")
else:
    print("Milk: empty")