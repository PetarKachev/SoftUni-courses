a = int(input())
b = int(input())
max_passwords = int(input())

available_passwords = max_passwords
no_more_passwords = False
A = 35
B = 64

for x in range(1, a + 1):
    for y in range(1, b + 1):
        if available_passwords == 0:
            no_more_passwords = True
            break
        print(f"{chr(A)}{chr(B)}{x}{y}{chr(B)}{chr(A)}|", end="")

        A += 1
        B += 1
        if A > 55:
            A = 35
        if B > 96:
            B = 64

        available_passwords -= 1

    if no_more_passwords:
        break

