skumriq_price = float(input())
caca_price = float(input())
palamud_kg = float(input())
safrid_kg = float(input())
shellfish_kg = float(input())

palamud_price = palamud_kg * (skumriq_price * 1.60)
safrid_price = safrid_kg * (caca_price * 1.80)
shellfish_price = shellfish_kg * 7.50

total_price = palamud_price + safrid_price + shellfish_price
print(f"{total_price:.2f}")
