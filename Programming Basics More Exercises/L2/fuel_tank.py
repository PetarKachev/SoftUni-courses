fuel_type = input()
liters = float(input())

if fuel_type == 'Diesel':
    if liters >= 25:
        print(f"You have enough diesel.")
    else:
        print(f"Fill your tank with diesel!")
elif fuel_type == 'Gasoline':
    if liters >= 25:
        print(f"You have enough gasoline.")
    else:
        print(f"Fill your tank with gasoline!")
elif fuel_type == 'Gas':
    if liters >= 25:
        print(f"You have enough gas.")
    else:
        print(f"Fill your tank with gas!")
else:
    print("Invalid fuel!")
