kilometers = int(input())
time = input()
price = 0

if kilometers < 20:
    if time == 'day':
        price = 0.70 + (kilometers * 0.79)
    if time == 'night':
        price = 0.70 + (kilometers * 0.90)
elif 20 <= kilometers < 100:
    price = kilometers * 0.09
else:
    price = kilometers * 0.06

print(f"{price:.2f}")
