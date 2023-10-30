items_list = input().split("|")
budget = float(input())

list_of_old_prices = []
list_of_new_prices = []

old_prices = 0
new_prices = 0

for item in items_list:
    modified_list = item.split("->")
    vetements = modified_list[0]
    prices = float(modified_list[1])

    if budget < prices:
        continue

    if vetements == "Clothes" and prices <= 50.00 and budget > 0:
        budget -= prices
        list_of_old_prices.append(prices)
        list_of_new_prices.append(f'{prices + (prices * 0.4):.2f}')
    elif vetements == "Shoes" and prices <= 35.00 and budget > 0:
        budget -= prices
        list_of_old_prices.append(prices)
        list_of_new_prices.append(f'{prices + (prices * 0.4):.2f}')
    elif vetements == "Accessories" and prices <= 20.50 and budget > 0:
        budget -= prices
        list_of_old_prices.append(prices)
        list_of_new_prices.append(f'{prices + (prices * 0.4):.2f}')

for i in list_of_old_prices:
    old_prices += float(i)

for j in list_of_new_prices:
    new_prices += float(j)
    print(j, end=" ")
print()

profit = new_prices - old_prices

final_budget = new_prices + budget

if final_budget >= 150:
    print(f"Profit: {profit:.2f}")
    print("Hello, France!")
else:
    print(f"Profit: {profit:.2f}")
    print("Not enough money.")

