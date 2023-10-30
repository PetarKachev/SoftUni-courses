int_strings = input().split(', ')
count_beggars = int(input())
integers_list = []
for current in int_strings:
    integers_list.append(int(current))

sum_list = []
start_index = 0

while start_index < count_beggars:
    current_sum = 0
    for index in range(start_index, len(integers_list), count_beggars):
        current_sum += integers_list[index]
    sum_list.append(current_sum)
    start_index += 1

print(sum_list)