from collections import deque
bowls = deque(list(map(int, input().split(", "))))
customers = deque(list(map(int, input().split(", "))))

while bowls and customers:
    if bowls[-1] == customers[0]:
        bowls.pop()
        customers.popleft()
    elif bowls[-1] > customers[0]:
        bowls[-1] -= customers.popleft()
        if bowls and customers:
            if bowls[-1] == customers[0]:
                bowls.pop()
                customers.popleft()
    elif bowls[-1] < customers[0]:
        customers[0] -= bowls.pop()
        if bowls and customers:
            if bowls[-1] == customers[0]:
                bowls.pop()
                customers.popleft()

if len(customers) == 0:
    print("Great job! You served all the customers.")
    if len(bowls) > 0:
        print(f"Bowls of ramen left: {', '.join(str(el) for el in bowls)}")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(str(el) for el in customers)}")