n = int(input())

for i in range(n):
    pure_or_not_pure = input()
    if "," in pure_or_not_pure or \
        "." in pure_or_not_pure or \
        "_" in pure_or_not_pure:
        print(f'{pure_or_not_pure} is not pure!')
    else:
        print(f'{pure_or_not_pure} is pure.')