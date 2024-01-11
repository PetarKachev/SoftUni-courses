n = int(input())

vip_guests = []
normal_guests = []

for i in range(n):
    current_guest = input()
    if current_guest[0].isdigit():
        if current_guest not in vip_guests:
            vip_guests.append(current_guest)
    else:
        if current_guest not in normal_guests:
            normal_guests.append(current_guest)

command = input()
while command != "END":
    if command in vip_guests:
        for element in range(len(vip_guests)):
            if vip_guests[element] == command:
                vip_guests.pop(element)
                break
    elif command in normal_guests:
        for element in range(len(normal_guests)):
            if normal_guests[element] == command:
                normal_guests.pop(element)
                break
    else:
        if command[0].isdigit():
            vip_guests.append(command)
        else:
            normal_guests.append(command)
    command = input()

vip_guests = sorted(vip_guests)
normal_guests = sorted(normal_guests)
for element in normal_guests:
    vip_guests.append(element)
print(len(vip_guests))
for current_element in vip_guests:
    print(current_element)