budget = int(input())
season = input()
fishermen = int(input())
ship_rent = 0

if season == 'Spring':
    ship_rent = 3000
elif season == 'Summer' or season == 'Autumn':
    ship_rent = 4200
elif season == 'Winter':
    ship_rent = 2600

if fishermen <= 6:
    ship_rent = ship_rent * 0.90
elif 6 < fishermen <= 11:
    ship_rent = ship_rent * 0.85
elif fishermen > 11:
    ship_rent = ship_rent * 0.75

if fishermen % 2 == 0 and season != 'Autumn':
    ship_rent = ship_rent * 0.95

diff = abs(budget - ship_rent)

if budget >= ship_rent:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")
