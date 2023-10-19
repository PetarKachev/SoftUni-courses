dog_foods_purchased = int(input())
cat_foods_purchased = int(input())

dog_food_price = 2.50
cat_food_price = 4.00

all_dog_foods_price = dog_foods_purchased * dog_food_price
all_cat_foods_price = cat_foods_purchased * cat_food_price

all_foods_price = (all_dog_foods_price) + (all_cat_foods_price)

print(f"{all_foods_price} lv.")