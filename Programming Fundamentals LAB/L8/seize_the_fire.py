type_of_fire = input().split("#")
water = int(input())

effort = 0
total_fire = 0
my_list = []

print("Cells:")

for fire in type_of_fire:
    modified_list = fire.split(" = ")
    fire_type = modified_list[0]
    level = modified_list[1]
    valid = False

    if water < int(level):
        continue

    if fire_type == "High":
        if 81 <= int(level) <= 125:
            my_list.append(level)
            valid = True
    elif fire_type == "Medium":
        if 51 <= int(level) <= 80:
            my_list.append(level)
            valid = True
    elif fire_type == "Low":
        if 1 <= int(level) <= 50:
            my_list.append(level)
            valid = True

    if valid:
        water -= int(level)
        effort += int(level) * 0.25
        total_fire += int(level)

for i in my_list:
    print(f' - {i}')

print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')