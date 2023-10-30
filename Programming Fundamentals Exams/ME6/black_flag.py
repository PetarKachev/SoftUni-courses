the_days_of_the_plunder = int(input())
daily_plunder = int(input())
expected_plunder = float(input())

all_plunder = 0

for i in range(1, the_days_of_the_plunder + 1):
    all_plunder += daily_plunder
    if i % 3 == 0:
        all_plunder += daily_plunder * 0.50
    if i % 5 == 0:
        all_plunder -= all_plunder * 0.30

if all_plunder >= expected_plunder:
    print(f"Ahoy! {all_plunder:.2f} plunder gained.")
else:
    print(f"Collected only {(all_plunder / expected_plunder) * 100:.2f}% of the plunder.")