number = input().split()

my_list = []

for i in number:
    my_list.append(int(i))

result = lambda x : x % 2 == 0

print(list(filter(result, my_list)))
