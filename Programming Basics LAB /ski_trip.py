days = int(input())
room = input()
mark = input()
price = 0

if room == 'room for one person':
    price = (days - 1) * 18
elif room == 'apartment':
    price = (days - 1) * 25
    if days < 10:
        price = price * 0.70
    elif 10 < days < 15:
        price = price * 0.65
    elif days > 15:
        price = price * 0.50
elif room == 'president apartment':
    price = (days - 1) * 35
    if days < 10:
        price = price * 0.90
    elif 10 < days < 15:
        price = price * 0.85
    elif days > 15:
        price = price * 0.80

if mark == 'positive':
    price = price * 1.25
elif mark == 'negative':
    price = price * 0.9

print(f"{price:.2f}")
