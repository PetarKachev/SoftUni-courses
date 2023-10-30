from math import ceil, floor

days = int(input())
food_left_kg = int(input())
dog_food_per_day_kg = float(input())
cat_food_per_day_kg = float(input())
turtle_food_per_day_g = float(input())

food_for_dog = dog_food_per_day_kg * days
food_for_cat = cat_food_per_day_kg * days
food_for_turtle = (turtle_food_per_day_g / 1000) * days
all_required_food = food_for_cat + food_for_turtle + food_for_dog

diff = abs(food_left_kg - all_required_food)

if all_required_food <= food_left_kg:
    print(f"{floor(diff)} kilos of food left.")
else:
    print(f"{ceil(diff)} more kilos of food are needed.")
