n = int(input())

liters_tank = 255

pour_liters = 0

for i in range(n):
    liter = int(input())
    if liters_tank - liter < 0:
        print(f'Insufficient capacity!')
        continue
    liters_tank -= liter
    pour_liters += liter

print(f'{pour_liters}')
