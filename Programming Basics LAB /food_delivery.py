chicken_menu = int(input())
fish_menu = int(input())
veggie_menu = int(input())

price_chicken = chicken_menu * 10.35
price_fish = fish_menu * 12.40
price_veggie = veggie_menu * 8.15

total_menu_price = price_chicken + price_fish + price_veggie
dessert = total_menu_price * 0.20

total_amount = total_menu_price + dessert + 2.50

print(total_amount)
