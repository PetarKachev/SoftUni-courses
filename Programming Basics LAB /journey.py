budget = float(input())
season = input()
place = ''
destination = ''
price = 0

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        price = budget * 0.30
    elif season == 'winter':
        price = budget * 0.70
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        price = budget * 0.40
    elif season == 'winter':
        price = budget * 0.80
elif budget > 1000:
    destination = 'Europe'
    if season == 'summer' or season == 'winter':
        price = budget * 0.90

if season == 'summer' and destination != 'Europe':
    place = 'Camp'
else:
    place = 'Hotel'

print(f"Somewhere in {destination}")
print(f"{place} - {price:.2f}")
