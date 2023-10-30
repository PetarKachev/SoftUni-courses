numbers = input().split(" ")

int_list = []
for i in numbers:
    int_list.append(int(i))

print(sorted(int_list))