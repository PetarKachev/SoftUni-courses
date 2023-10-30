first_sequence = input().split(", ")
second_sequence = input().split(", ")
new_list = []

for i in first_sequence:
    for j in second_sequence:
        if i in j and not i in new_list:
            new_list.append(i)

print(new_list)
