start_interval = int(input())
final_interval = int(input())
n = int(input())
combinations = 0
break_condition = False

for x in range(start_interval, final_interval + 1):
    for y in range(start_interval, final_interval + 1):
        combinations += 1

        if x + y == n:
            break_condition = True
            print(f"Combination N:{combinations} ({x} + {y} = {n})")
            break

    if break_condition:
        break

else:
    print(f"{combinations} combinations - neither equals {n}")
