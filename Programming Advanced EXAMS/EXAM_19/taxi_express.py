from collections import deque
customers = deque(list(map(int, input().split(", "))))
taxis = deque(list(map(int, input().split(", "))))
total_time = 0

while customers and taxis:

    if customers[0] <= taxis[-1]:
        total_time += customers[0]
        customers.popleft()
        taxis.pop()
    else:
        taxis.pop()

if len(customers) == 0:
    print('All customers were driven to their destinations')
    print(f'Total time: {total_time} minutes')

elif len(customers) > 0 and len(taxis) == 0:
    print(f'Not all customers were driven to their destinations')
    print(f'Customers left: {", ".join(str(el) for el in customers)}')