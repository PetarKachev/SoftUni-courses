M = int(input())

pass_counter = 0
password = ''
pass_flag = False

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if a >= b or c <= d:
                    continue
                if (a * b) + (c * d) == M:
                    print(f"{a}{b}{c}{d}", end=" ")
                    pass_counter += 1
                    if pass_counter == 4:
                        password = (str(a) + str(b) + str(c) + str(d))
                        pass_flag = True
print()     # Нов ред
if pass_flag:
    print(f"Password: {password}")
else:
    print(f"No!")
