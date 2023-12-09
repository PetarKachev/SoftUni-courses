n = int(input())
dictionary = {}
for i in range(n):
    input_info = input()
    input_info = input_info.split("|")
    car = input_info[0]
    mileage = int(input_info[1])
    fuel = int(input_info[2])
    if car not in dictionary.keys():
        dictionary[car] = []
        dictionary[car].append(mileage)
        dictionary[car].append(fuel)
command = input()

while command != "Stop":
    command = command.split(" : ")
    if command[0] == "Drive":
        car = command[1]
        mileage = int(command[2])
        fuel = int(command[3])
        if dictionary[car][1] < fuel:
            print(f"Not enough fuel to make that ride")
        elif dictionary[car][1] >= fuel:
            dictionary[car][0] += mileage
            dictionary[car][1] -= fuel
            print(f"{car} driven for {mileage} kilometers. {fuel} liters of fuel consumed.")
        if dictionary[car][0] >= 100000:
            del dictionary[car]
            print(f"Time to sell the {car}!")

    elif command[0] == "Refuel":
        car = command[1]
        fuel = int(command[2])
        if dictionary[car][1] + fuel >= 75:
            print(f"{car} refueled with {75 - dictionary[car][1]} liters")
            dictionary[car][1] = 75
        else:
            dictionary[car][1] += fuel
            print(f"{car} refueled with {fuel} liters")

    elif command[0] == "Revert":
        car = command[1]
        mileage = int(command[2])
        dictionary[car][0] -= mileage
        if dictionary[car][0] < 10000:
            dictionary[car][0] = 10000
        else:
            print(f"{car} mileage decreased by {mileage} kilometers")
    command = input()
for key, value in dictionary.items():
    print(f"{key} -> Mileage: {value[0]} kms, Fuel in the tank: {value[1]} lt.")