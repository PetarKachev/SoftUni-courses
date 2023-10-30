budget = float(input())
category = input()
people_in_group = int(input())

ticket_price = 0
transportation_price = 0

if category == 'Normal':
    ticket_price = 249.99
    if 1 <= people_in_group <= 4:
        transportation_price = budget * 0.75
    elif 5 <= people_in_group <= 9:
        transportation_price = budget * 0.60
    elif 10 <= people_in_group <= 24:
        transportation_price = budget * 0.50
    elif 25 <= people_in_group <= 49:
        transportation_price = budget * 0.40
    elif people_in_group >= 50:
        transportation_price = budget * 0.25
elif category == 'VIP':
    ticket_price = 499.99
    if 1 <= people_in_group <= 4:
        transportation_price = budget * 0.75
    elif 5 <= people_in_group <= 9:
        transportation_price = budget * 0.60
    elif 10 <= people_in_group <= 24:
        transportation_price = budget * 0.50
    elif 25 <= people_in_group <= 49:
        transportation_price = budget * 0.40
    elif people_in_group >= 50:
        transportation_price = budget * 0.25

all_tickets_price = people_in_group * ticket_price
total_price = all_tickets_price + transportation_price
diff = abs(budget - total_price)

if budget >= total_price:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")
