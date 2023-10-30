fuel_type = input()
fuel_lt = float(input())
club_card = input()

price_fuel = 0

if club_card == "Yes":
    if fuel_type == "Diesel":
        price_fuel = fuel_lt * 2.21
    elif fuel_type == "Gasoline":
        price_fuel = fuel_lt * 2.04
    elif fuel_type == "Gas":
        price_fuel = fuel_lt * 0.85
else:
    if fuel_type == "Diesel":
        price_fuel = fuel_lt * 2.33
    elif fuel_type == "Gasoline":
        price_fuel = fuel_lt * 2.22
    elif fuel_type == "Gas":
        price_fuel = fuel_lt * 0.93

if 20 <= fuel_lt <= 25:
    price_fuel *= 0.92
elif fuel_lt > 25:
    price_fuel *= 0.90

print(f"{price_fuel:.2f} lv.")