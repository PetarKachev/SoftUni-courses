string = input().split()
count_shuffles = int(input())

for element in range(count_shuffles):
    middle_deck = len(string) // 2
    left_part = string[:middle_deck]
    right_part = string[middle_deck:]
    shuffled_list = []
    for index in range(len(left_part)):
        shuffled_list.append(left_part[index])
        shuffled_list.append(right_part[index])
    string = shuffled_list

print(shuffled_list)
