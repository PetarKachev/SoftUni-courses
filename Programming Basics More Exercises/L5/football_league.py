stadium_capacity = int(input())
total_fans = int(input())

A_counter = 0
B_counter = 0
V_counter = 0
G_counter = 0

for _ in range(total_fans):
    sector = input()
    if sector == 'A':
        A_counter += 1
    elif sector == 'B':
        B_counter += 1
    elif sector == 'V':
        V_counter += 1
    elif sector == 'G':
        G_counter += 1

sector_A_percent = A_counter / total_fans * 100
sector_B_percent = B_counter / total_fans * 100
sector_V_percent = V_counter / total_fans * 100
sector_G_percent = G_counter / total_fans * 100
fans_to_capacity = total_fans / stadium_capacity * 100

print(f"{sector_A_percent:.2f}%")
print(f"{sector_B_percent:.2f}%")
print(f"{sector_V_percent:.2f}%")
print(f"{sector_G_percent:.2f}%")
print(f"{fans_to_capacity:.2f}%")
