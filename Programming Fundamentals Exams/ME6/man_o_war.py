pirate_ship_status = list(map(int, input().split(">")))
warship_status = list(map(int, input().split(">")))
maximum_health = int(input())

command = input()

while command != "Retire":
    command = command.split(" ")
    if command[0] == "Fire":
        index = int(command[1])
        damage = int(command[2])

        if index >= 0 and index < len(warship_status):
            warship_status[index] -= damage
            if warship_status[index] <= 0:
                print("You won! The enemy ship has sunken.")
                exit()

    elif command[0] == "Defend":
        start_index = int(command[1])
        end_index = int(command[2])
        damage = int(command[3])

        if start_index >= 0 and start_index < len(pirate_ship_status) and end_index >= 0 and end_index < len(pirate_ship_status):
            for j in range(start_index, end_index + 1):
                pirate_ship_status[j] -= damage
            for i in range(len(pirate_ship_status)):
                if pirate_ship_status[i] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    exit()

    elif command[0] == "Repair":
        index = int(command[1])
        health = int(command[2])

        if index >= 0 and index < len(pirate_ship_status):
            pirate_ship_status[index] += health
            if pirate_ship_status[index] > maximum_health:
                pirate_ship_status[index] = maximum_health

    elif command[0] == "Status":
        sections_for_repair = 0
        for i in range(len(pirate_ship_status)):
            if pirate_ship_status[i] < maximum_health * 0.20:
                sections_for_repair += 1
        print(f"{sections_for_repair} sections need repair.")


    command = input()

print(f"Pirate ship status: {sum(pirate_ship_status)}")
print(f"Warship status: {sum(warship_status)}")