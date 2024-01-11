n = int(input())

parking = []

for i in range(n):
    command = input().split(", ")
    direction = command[0]
    car_number = command[1]

    if direction == "IN":
        if car_number not in parking:
            parking.append(car_number)
    elif direction == "OUT":
        if car_number in parking:
            car_index = parking.index(car_number)
            parking.pop(car_index)
if len(parking) > 0:
    for car in parking:
        print(car)
else:
    print("Parking Lot is Empty")