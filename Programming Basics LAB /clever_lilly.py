age = int(input())
wash_price = float(input())
toy_price = int(input())

saved_money = 0
toys = 0
money_in_brother = 0

for year in range (1, age + 1):
    if year % 2 == 0:
        saved_money += int(year / 2) * 10
        money_in_brother += 1
    else:
        toys += 1

toys_money = toys * toy_price
total_money = saved_money + toys_money - money_in_brother
diff = abs(total_money - wash_price)

if total_money >= wash_price:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")