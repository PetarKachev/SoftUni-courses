input_info = input().split(" ")

bakery = {}

for i in range(0, len(input_info), 2):
    key = input_info[i]
    value = input_info[i + 1]
    bakery[key] = int(value)

print(bakery)