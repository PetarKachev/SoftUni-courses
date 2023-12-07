import re
text = input()
regex = r'([#|])([A-Za-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1'
matches = re.finditer(regex, text)
all_calories = 0

for match in matches:
    product = match.group(2)
    date = match.group(3)
    calories = int(match.group(4))
    all_calories += calories
days_to_survive = all_calories // 2000
print(f'You have food to last you for: {days_to_survive} days!')

regex = r'([#|])([A-Za-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1'
matches = re.finditer(regex, text)

for food in matches:
    product = food.group(2)
    date = food.group(3)
    calories = int(food.group(4))
    print(f"Item: {product}, Best before: {date}, Nutrition: {calories}")