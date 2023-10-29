entry_num = int(input())
end_num = int(input())
n = int(input())
combination = 0
a, b = 0, 0
condition_break = False

for x1 in range(entry_num, end_num + 1):
    for x2 in range(entry_num, end_num + 1):
        result = x1 + x2
        combination += 1
        if result == n:
            a = x1
            b = x2
            condition_break = True
            break

    if condition_break:
        break

if condition_break:
    print(f"Combination N:{combination} ({a} + {b} = {n})")
else:
    print(f"{combination} combinations - neither equals {n}")
