from collections import deque

monsters_armor = deque(list(map(int, input().split(","))))
soldier_damage = deque(list(map(int, input().split(","))))
start_len_monster = len(monsters_armor)
start_len_soldier = len(soldier_damage)

while monsters_armor and soldier_damage:
    if len(monsters_armor) == 0 or len(soldier_damage) == 0:
        break

    if soldier_damage[-1] >= monsters_armor[0]:
        soldier_damage[-1] -= monsters_armor.popleft()
        element_for_add = soldier_damage.pop()

        if len(soldier_damage) > 0:
            soldier_damage[-1] += int(element_for_add)
        else:
            if element_for_add > 0:
                soldier_damage.append(element_for_add)
    else:
        monsters_armor.append(monsters_armor.popleft() - soldier_damage.pop())

if len(monsters_armor) == 0:
    print("All monsters have been killed!")
if len(soldier_damage) == 0:
    print("The soldier has been defeated.")
print(f"Total monsters killed: {start_len_monster - len(monsters_armor)}")
