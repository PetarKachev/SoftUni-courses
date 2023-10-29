type_flower = input()
flower_count = int(input())
budget = int(input())
total_price = 0

if type_flower == 'Roses':
    if flower_count > 80:
        total_price = (flower_count * 5.00) * 0.90
    else:
        total_price = flower_count * 5.00
elif type_flower == 'Dahlias':
    if flower_count > 90:
        total_price = (flower_count * 3.80) * 0.85
    else:
        total_price = flower_count * 3.80
elif type_flower == 'Tulips':
    if flower_count > 80:
        total_price = (flower_count * 2.80) * 0.85
    else:
        total_price = flower_count * 2.80
elif type_flower == 'Narcissus':
    if flower_count < 120:
        total_price = (flower_count * 3.00) * 1.15
    else:
        total_price = flower_count * 3.00
elif type_flower == 'Gladiolus':
    if flower_count < 80:
        total_price = (flower_count * 2.50) * 1.20
    else:
        total_price = flower_count * 2.50

diff = abs(budget - total_price)
if total_price <= budget:
    print(f"Hey, you have a great garden with {flower_count} {type_flower} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")