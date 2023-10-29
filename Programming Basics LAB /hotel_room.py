month = input()
days = int(input())
studio_price = 0
apt_price = 0

if month == 'May' or month == 'October':
    studio_price = 50 * days
    apt_price = 65 * days
elif month == 'June' or month == 'September':
    studio_price = 75.20 * days
    apt_price = 68.70 * days
elif month == 'July' or month == 'August':
    studio_price = 76 * days
    apt_price = 77 * days

if month == 'May' or month == 'October':
    if 7 < days < 14:
        studio_price = studio_price * 0.95
    elif days > 14:
        studio_price = studio_price * 0.70
elif month == 'June' or month == 'September':
    if days > 14:
        studio_price = studio_price * 0.80

if days > 14:
    apt_price = apt_price * 0.90

print(f"Apartment: {apt_price:.2f} lv.")
print(f"Studio: {studio_price:.2f} lv.")
