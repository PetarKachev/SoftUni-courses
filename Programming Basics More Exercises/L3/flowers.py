chrysanthemums_bought = int(input())
roses_bought = int(input())
tulips_bought = int(input())
season = input()
is_the_day_holiday = input()

all_flowers = chrysanthemums_bought + roses_bought + tulips_bought

bouquet_price = 0

if season == "Spring" or season == "Summer":
    bouquet_price += chrysanthemums_bought * 2
    bouquet_price += roses_bought * 4.10
    bouquet_price += tulips_bought * 2.50
elif season == "Autumn" or season == "Winter":
    bouquet_price += chrysanthemums_bought * 3.75
    bouquet_price += roses_bought * 4.50
    bouquet_price += tulips_bought * 4.15

if is_the_day_holiday == "Y":
    bouquet_price *= 1.15
if season == "Spring" and tulips_bought > 7:
    bouquet_price *= 0.95
if season == "Winter" and roses_bought >= 10:
    bouquet_price *= 0.90
if all_flowers > 20:
    bouquet_price *= 0.80

bouquet_price += 2

print(f"{bouquet_price:.2f}")
