n = int(input())
unique_names = []
for i in range(n):
    name = input()
    if name not in unique_names:
        unique_names.append(name)
for name in unique_names:
    print(name)