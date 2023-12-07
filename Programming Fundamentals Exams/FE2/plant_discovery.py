n = int(input())
dictionary = {}
for i in range(n):
    plant_info = input()
    plant_info = plant_info.split("<->")
    plant = plant_info[0]
    rarity = int(plant_info[1])
    if not plant in dictionary.keys():
        dictionary[plant] = {"rarity": rarity, "rating": 0, "count": 0}
    else:
        dictionary[plant]["rarity"] = rarity
command = input()

while command != "Exhibition":
    command = command.split(": ")
    if command[0] == "Rate":
        plant_and_rating = command[1].split(" - ")
        plant = plant_and_rating[0]
        rating = float(plant_and_rating[1])

        if plant in dictionary.keys():
            dictionary[plant]["rating"] += rating
            dictionary[plant]["count"] += 1
        else:
            print("error")

    elif command[0] == "Update":
        plant_and_new_rarity = command[1].split(" - ")
        plant = plant_and_new_rarity[0]
        new_rarity = int(plant_and_new_rarity[1])

        if plant in dictionary.keys():
            dictionary[plant]["rarity"] = new_rarity
        else:
            print("error")

    elif command[0] == "Reset":
        plant = command[1]

        if plant in dictionary.keys():
            dictionary[plant]["rating"] = 0
            dictionary[plant]["count"] = 0
        else:
            print("error")

    command = input()

print(f'Plants for the exhibition:')

for key, value in dictionary.items():
    current_rating = value["rating"]
    current_count = value["count"]
    average_rating = 0
    if current_rating == 0 or current_count == 0:
        average_rating = 0
    else:
        average_rating = current_rating / current_count

    print(f'- {key}; Rarity: {value["rarity"]}; Rating: {average_rating:.2f}')