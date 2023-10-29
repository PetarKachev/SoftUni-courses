city = input()
sales_volume = float(input())
commision = 0

if city == 'Sofia':
    if 0 <= sales_volume <= 500:
        commision = 0.05
    elif 500 < sales_volume <= 1000:
        commision = 0.07
    elif 1000 < sales_volume <= 10000:
        commision = 0.08
    elif sales_volume > 10000:
        commision = 0.12
elif city == 'Varna':
    if 0 <= sales_volume <= 500:
        commision = 0.045
    elif 500 < sales_volume <= 1000:
        commision = 0.075
    elif 1000 < sales_volume <= 10000:
        commision = 0.10
    elif sales_volume > 10000:
        commision = 0.13
elif city == 'Plovdiv':
    if 0 <= sales_volume <= 500:
        commision = 0.055
    elif 500 < sales_volume <= 1000:
        commision = 0.08
    elif 1000 < sales_volume <= 10000:
        commision = 0.12
    elif sales_volume > 10000:
        commision = 0.145

income = sales_volume * commision

if not (city == 'Sofia' or city == 'Varna' or city == 'Plovdiv') or sales_volume < 0:
    print('error')
else:
    print(f'{income:.2f}')
