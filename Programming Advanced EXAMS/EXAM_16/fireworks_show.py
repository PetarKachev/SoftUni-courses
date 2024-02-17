from collections import deque
fire_work_effects = deque(list(map(int, input().split(", "))))
explosive_powers = deque(list(map(int, input().split(", "))))
items = {"Palm Fireworks": 0, "Willow Fireworks": 0, "Crossette Fireworks": 0}
items_collected = False

while fire_work_effects and explosive_powers:

    while fire_work_effects[0] <= 0:
        fire_work_effects.popleft()
        if len(fire_work_effects) == 0:
            break

    while explosive_powers[-1] <= 0:
        explosive_powers.pop()
        if len(explosive_powers) == 0:
            break

    if len(fire_work_effects) == 0 or len(explosive_powers) == 0:
        break

    sum = fire_work_effects[0] + explosive_powers[-1]

    if sum % 3 == 0 and sum % 5 != 0:
        items["Palm Fireworks"] += 1
        fire_work_effects.popleft()
        explosive_powers.pop()

    elif sum % 5 == 0 and sum % 3 != 0:
        items["Willow Fireworks"] += 1
        fire_work_effects.popleft()
        explosive_powers.pop()

    elif sum % 3 == 0 and sum % 5 == 0:
        items["Crossette Fireworks"] += 1
        fire_work_effects.popleft()
        explosive_powers.pop()

    else:
        fire_work_effects.append(fire_work_effects.popleft() - 1)

    if items["Palm Fireworks"] >= 3 and items["Willow Fireworks"] >= 3 and items["Crossette Fireworks"] >= 3:
        items_collected = True
        break

if items_collected == True:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if len(fire_work_effects) > 0:
    print(f"Firework Effects left: {', '.join(str(el) for el in fire_work_effects)}")
if len(explosive_powers) > 0:
    print(f"Explosive Power left: {', '.join(str(el) for el in explosive_powers)}")
print(f'Palm Fireworks: {items["Palm Fireworks"]}')
print(f'Willow Fireworks: {items["Willow Fireworks"]}')
print(f'Crossette Fireworks: {items["Crossette Fireworks"]}')