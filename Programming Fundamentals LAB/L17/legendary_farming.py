inventory = {"shards": 0,
             "fragments": 0,
             "motes": 0,
             "junk": {}
             }

is_item_found = False

while True:
    if is_item_found:
        break

    information = input().split(" ")

    for i in range(0, len(information), 2):
        quantity = int(information[i])
        item = information[i + 1]
        item = item.lower()

        if item in inventory.keys():
            inventory[item] += quantity
            if inventory[item] >= 250:
                is_item_found = True

            if inventory["shards"] >= 250:
                print('Shadowmourne obtained!')
                inventory[item] -= 250
                break

            elif inventory["fragments"] >= 250:
                print('Valanyr obtained!')
                inventory[item] -= 250
                break

            elif inventory["motes"] >= 250:
                print('Dragonwrath obtained!')
                inventory[item] -= 250
                break

        else:
            if item not in inventory["junk"]:
                inventory["junk"][item] = quantity
            else:
                inventory["junk"][item] += quantity

print(f'shards: {inventory["shards"]}')
print(f'fragments: {inventory["fragments"]}')
print(f'motes: {inventory["motes"]}')

for key, value in inventory["junk"].items():
    print(f'{key}: {value}')