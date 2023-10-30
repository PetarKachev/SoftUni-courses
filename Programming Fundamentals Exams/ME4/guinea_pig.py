quantity_food_kg = float(input())
quantity_hay_kg = float(input())
quantity_cover_kg = float(input())
guinea_weight = float(input())
quantity_food_grams = quantity_food_kg * 1000
quantity_hay_grams = quantity_hay_kg * 1000
quantity_cover_grams = quantity_cover_kg * 1000
guinea_weight_grams = guinea_weight * 1000
days = 0
import sys
while quantity_food_grams > 0 and quantity_hay_grams > 0 and quantity_cover_grams > 0:
    days += 1
    quantity_food_grams -= 300
    if days % 2 == 0:
        quantity_hay_grams -= (quantity_food_grams * 0.05)
    if days % 3 == 0:
        quantity_cover_grams -= (guinea_weight_grams / 3)
    if days == 30:
        break
if days == 30 and quantity_food_grams > 0 and quantity_hay_grams > 0 and quantity_cover_grams:
    print(f"Everything is fine! Puppy is happy! Food: {(quantity_food_grams / 1000):.2f}, Hay: {(quantity_hay_grams / 1000):.2f}, Cover: {(quantity_cover_grams / 1000):.2f}.")
else:
    print('Merry must go to the pet store!')