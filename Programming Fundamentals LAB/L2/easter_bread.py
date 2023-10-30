budget = float(input())
price_1_kg_flour = float(input())
one_pack_eggs = price_1_kg_flour * 0.75
price_for_one_liter_milk = price_1_kg_flour * 1.25
price_milk_250_ml = price_for_one_liter_milk / 4
price_one_loaf = price_1_kg_flour + one_pack_eggs + price_milk_250_ml
colored_eggs = 0
loafs = 0
while budget > price_one_loaf:
    loafs += 1
    colored_eggs += 3
    budget -= price_one_loaf
    if loafs % 3 == 0:
        colored_eggs -= (loafs - 2)
print(f'You made {loafs} loaves of Easter bread! Now you have {colored_eggs} eggs and {abs(budget):.2f}BGN left.')


