from collections import deque
order = deque(list(map(int, input().split(", "))))
employee = deque(list(map(int, input().split(", "))))
pizzas_made = 0

while order and employee:

    while 0 >= order[0] or order[0] > 10:
        order.popleft()
        if len(order) == 0:
            break

    if len(order) == 0 or len(employee) == 0:
        break

    if order[0] <= employee[-1]:
        pizzas_made += order[0]
        order.popleft()
        employee.pop()

    elif order[0] > employee[-1]:
        if len(employee) > 0:
            pizzas_made += employee[-1]
            order[0] -= employee.pop()
        else:
            break

if len(order) == 0:
    print('All orders are successfully completed!')
    print(f'Total pizzas made: {pizzas_made}')
    print(f'Employees: {", ".join(str(el) for el in employee)}')
else:
    print('Not all orders are completed.')
    print(f'Orders left: {", ".join(str(el) for el in order)}')
