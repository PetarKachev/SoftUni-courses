n = int(input())
dictionary = {}
for i in range(n):
    input_info = input()
    input_info = input_info.split(" ")
    hero = input_info[0]
    hp = int(input_info[1])
    mp = int(input_info[2])
    if hero not in dictionary.keys():
        dictionary[hero] = []
        dictionary[hero].append(hp)
        dictionary[hero].append(mp)
command = input()
while command != "End":
    command = command.split(" - ")
    if command[0] == "CastSpell":
        hero_name = command[1]
        mana_points = int(command[2])
        spell_name = command[3]
        if dictionary[hero_name][1] >= mana_points:
            dictionary[hero_name][1] -= mana_points
            print(f"{hero_name} has successfully cast {spell_name} and now has {dictionary[hero_name][1]} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    elif command[0] == "TakeDamage":
        hero_name = command[1]
        damage = int(command[2])
        attacker = command[3]
        dictionary[hero_name][0] -= damage
        if dictionary[hero_name][0] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {dictionary[hero_name][0]} HP left!")
        else:
            del dictionary[hero_name]
            print(f"{hero_name} has been killed by {attacker}!")

    elif command[0] == "Recharge":
        hero_name = command[1]
        amount = int(command[2])
        if dictionary[hero_name][1] + amount > 200:
            print(f"{hero_name} recharged for {200 - dictionary[hero_name][1]} MP!")
            dictionary[hero_name][1] = 200
        else:
            dictionary[hero_name][1] += amount
            print(f"{hero_name} recharged for {amount} MP!")

    elif command[0] == "Heal":
        hero_name = command[1]
        amount = int(command[2])
        if dictionary[hero_name][0] + amount > 100:
            print(f"{hero_name} healed for {100 - dictionary[hero_name][0]} HP!")
            dictionary[hero_name][0] = 100
        else:
            dictionary[hero_name][0] += amount
            print(f"{hero_name} healed for {amount} HP!")
    command = input()
for key, value in dictionary.items():
    print(f'{key}')
    print(f'HP: {value[0]}')
    print(f'MP: {value[1]}')