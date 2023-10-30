command = input()
total_price_without_taxes = 0
taxes = 0
while True:
    if command == "special" or command == "regular":
        break
    price = float(command)
    if price < 0:
        print("Invalid price!")
        price -= price
    total_price_without_taxes += price
    taxes += price * 0.20
    command = input()
import sys
total_price = total_price_without_taxes + taxes
if total_price == 0:
    print("Invalid order!")
    sys.exit()
if command == "special":
    total_price -= (total_price * 0.10)
print("Congratulations you've just bought a new computer!")
print(f"Price without taxes: {total_price_without_taxes:.2f}$")
print(f"Taxes: {taxes:.2f}$")
print('-----------')
print(f'Total price: {total_price:.2f}$')
