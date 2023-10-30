lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

times_broken_helmet = lost_fights // 2
times_broken_sword = lost_fights // 3
times_broken_shield = lost_fights // ( 2 * 3 )
times_broken_armor = times_broken_shield // 2

print(f"Gladiator expenses: {(times_broken_helmet * helmet_price) + (times_broken_sword * sword_price) + (times_broken_shield * shield_price) + (times_broken_armor * armor_price):.2f} aureus")
