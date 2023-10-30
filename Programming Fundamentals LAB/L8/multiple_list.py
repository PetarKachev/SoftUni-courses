factor = int(input())
count = int(input())

my_list = []

for number in range(factor, factor * count + 1, factor):
    my_list.append(number)

print(my_list)