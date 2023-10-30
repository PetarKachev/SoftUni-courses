initial_health = 100
initial_bitcoin = 0
number_of_rooms = 0
dungeons_room = list(map(str, input().split("|")))

for i in range(len(dungeons_room)):
    current_element = dungeons_room[i].split(" ")
    room = str(current_element[0])
    points = int(current_element[1])
    number_of_rooms += 1

    if room == "potion":
        initial_health += points
        if initial_health > 100:
            print(f"You healed for {100 - (initial_health - points)} hp.")
            initial_health = 100
        else:
            print(f"You healed for {points} hp.")
        print(f"Current health: {initial_health} hp.")

    elif room == "chest":
        initial_bitcoin += points
        print(f"You found {points} bitcoins.")

    else:
        initial_health -= points
        if initial_health > 0:
            print(f"You slayed {room}.")
        else:
            print(f"You died! Killed by {room}.")
            break

if initial_health > 0 and number_of_rooms == len(dungeons_room):
    print("You've made it!")
    print(f'Bitcoins: {initial_bitcoin}')
    print(f"Health: {initial_health}")
else:
    print(f"Best room: {number_of_rooms}")