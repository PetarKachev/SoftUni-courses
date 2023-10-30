numbers = input().split(" ")

new_list = []

for num in numbers:
    new_list.append(abs(float(num)))

print(new_list)