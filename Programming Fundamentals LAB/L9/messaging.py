sequences_of_numbers = input().split(" ")
string = input()

message_list = []

for sequence in sequences_of_numbers:
    current_sum_from_sequence_numbers = 0
    for num in sequence:
        current_sum_from_sequence_numbers += int(num)

    current_sum_from_sequence_numbers %= len(string)
    message_list.append(string[current_sum_from_sequence_numbers])
    string = string.replace(string[current_sum_from_sequence_numbers], '', 1)

print(''.join(message_list))