inherited_money = float(input())
year_to_live = int(input())

current_age = 17
money_spent = 0

for i in range (1800, year_to_live + 1):
    current_age += 1
    if i % 2 == 0:
        money_spent += 12000
    else:
        money_spent += 12000 + (50 * current_age)

diff = abs(inherited_money - money_spent)

if inherited_money >= money_spent:
    print(f"Yes! He will live a carefree life and will have {diff:.2f} dollars left.")
else:
    print(f"He will need {diff:.2f} dollars to survive.")
