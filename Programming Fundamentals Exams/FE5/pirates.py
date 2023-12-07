command_1 = input()
dictionary = {}
while command_1 != "Sail":
    command_1 = command_1.split("||")
    city = command_1[0]
    population = int(command_1[1])
    gold = int(command_1[2])
    if city not in dictionary.keys():
        dictionary[city] = []
        dictionary[city].append(population)
        dictionary[city].append(gold)
    else:
        dictionary[city][0] += population
        dictionary[city][1] += gold
    command_1 = input()
command_2 = input()
while command_2 != "End":
    command_2 = command_2.split("=>")
    if command_2[0] == "Plunder":
        town = command_2[1]
        people = int(command_2[2])
        gold = int(command_2[3])
        if town in dictionary.keys():
            dictionary[town][0] -= people
            dictionary[town][1] -= gold
            print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
            if dictionary[town][0] <= 0 or dictionary[town][1] <= 0:
                del dictionary[town]
                print(f"{town} has been wiped off the map!")
    elif command_2[0] == "Prosper":
        town = command_2[1]
        gold = int(command_2[2])
        if town in dictionary.keys():
            if gold >= 0:
                dictionary[town][1] += gold
                print(f"{gold} gold added to the city treasury. {town} now has {dictionary[town][1]} gold.")
            else:
                print(f"Gold added cannot be a negative number!")
    command_2 = input()
if len(dictionary) > 0:
    print(f"Ahoy, Captain! There are {len(dictionary)} wealthy settlements to go to:")
    for key, value in dictionary.items():
        print(f'{key} -> Population: {value[0]} citizens, Gold: {value[1]} kg')
else:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")