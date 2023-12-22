dragons = {}

default_health = 250
default_damage = 45
default_armor = 10

n = int(input())
for _ in range(n):
    line = input().split()
    d_type = line[0]
    d_name = line[1]
    damage = line[2]
    health = line[3]
    armor = line[4]

    if damage == 'null':
        damage = default_damage
    else:
        damage = int(damage)

    if health == 'null':
        health = default_health
    else:
        health = int(health)

    if armor == 'null':
        armor = default_armor
    else:
        armor = int(armor)

    if d_type not in dragons.keys():
        dragons[d_type] = {d_name: {'damage': damage, 'health': health, 'armor': armor}}
    elif d_name not in dragons[d_type].keys():
        dragons[d_type][d_name] = {'damage': damage, 'health': health, 'armor': armor}
    elif d_name in dragons[d_type].keys():
        dragons[d_type][d_name] = {'damage': damage, 'health': health, 'armor': armor}

for curr_type in dragons.keys():
    curr_total_dmg = 0
    curr_total_health = 0
    curr_total_armor = 0
    for curr_name in dragons[curr_type].keys():
        curr_total_dmg += dragons[curr_type][curr_name]['damage']
        curr_total_health += dragons[curr_type][curr_name]['health']
        curr_total_armor += dragons[curr_type][curr_name]['armor']
    avg_dmg = curr_total_dmg / len(dragons[curr_type].keys())
    avg_health = curr_total_health / len(dragons[curr_type].keys())
    avg_armor = curr_total_armor / len(dragons[curr_type].keys())

    print(f"{curr_type}::({avg_dmg:.2f}/{avg_health:.2f}/{avg_armor:.2f})")
    for curr_name in sorted(dragons[curr_type].keys()):
        this_damage = dragons[curr_type][curr_name]['damage']
        this_health = dragons[curr_type][curr_name]['health']
        this_armor = dragons[curr_type][curr_name]['armor']
        print(f"-{curr_name} -> damage: {this_damage}, health: {this_health}, armor: {this_armor}")