season = input()
km_per_month = float(input())

income_per_km = 0

if season == 'Spring' or season == 'Autumn':
    if km_per_month <= 5000:
        income_per_km = 0.75
    elif 5000 < km_per_month <= 10000:
        income_per_km = 0.95
    elif 10000 < km_per_month <= 20000:
        income_per_km = 1.45
elif season == 'Summer':
    if km_per_month <= 5000:
        income_per_km = 0.90
    elif 5000 < km_per_month <= 10000:
        income_per_km = 1.10
    elif 10000 < km_per_month <= 20000:
        income_per_km = 1.45
elif season == 'Winter':
    if km_per_month <= 5000:
        income_per_km = 1.05
    elif 5000 < km_per_month <= 10000:
        income_per_km = 1.25
    elif 10000 < km_per_month <= 20000:
        income_per_km = 1.45

income_per_month = income_per_km * km_per_month
total_income = (income_per_month * 4) * 0.90

print(f"{total_income:.2f}")
