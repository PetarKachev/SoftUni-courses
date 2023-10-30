season = input()
group_type = input()
number_of_students = int(input())
days = int(input())

practiced_sport = ""
price_per_student = 0

if season == 'Winter':
    if group_type == 'girls':
        price_per_student = 9.60
        practiced_sport = "Gymnastics"
    elif group_type == 'boys':
        price_per_student = 9.60
        practiced_sport = "Judo"
    elif group_type == 'mixed':
        price_per_student = 10
        practiced_sport = "Ski"
elif season == 'Spring':
    if group_type == 'girls':
        price_per_student = 7.20
        practiced_sport = "Athletics"
    elif group_type == 'boys':
        price_per_student = 7.20
        practiced_sport = "Tennis"
    elif group_type == 'mixed':
        price_per_student = 9.50
        practiced_sport = "Cycling"
elif season == 'Summer':
    if group_type == 'girls':
        price_per_student = 15
        practiced_sport = "Volleyball"
    elif group_type == 'boys':
        price_per_student = 15
        practiced_sport = "Football"
    elif group_type == 'mixed':
        price_per_student = 20
        practiced_sport = "Swimming"

price_of_stay = number_of_students * price_per_student * days
discount = 0

if number_of_students >= 50:
    discount = 50
elif 20 <= number_of_students < 50:
    discount = 15
elif 20 > number_of_students >= 10:
    discount = 5

total_price = price_of_stay * (1 - (discount / 100))

print(f"{practiced_sport} {total_price:.2f} lv.")
