quantity = int(input())
days_until_christmas = int(input())

money = 0
christmas_spirit = 0
ornament_set = 2
tree_skirt = 5
tree_garland = 3
tree_lights = 15

for day in range(1, days_until_christmas + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        money += ornament_set * quantity
        christmas_spirit += 5
    if day % 3 == 0:
        money += quantity * (tree_skirt + tree_garland)
        christmas_spirit += 13
    if day % 5 == 0:
        money += tree_lights * quantity
        christmas_spirit += 17
        if day % 3 == 0:
            christmas_spirit += 30
    if day % 10 == 0:
        christmas_spirit -= 20
        money += tree_skirt + tree_garland + tree_lights

if days_until_christmas % 10 == 0:
    christmas_spirit -= 30
print(f'Total cost: {money}')
print(f'Total spirit: {christmas_spirit}')