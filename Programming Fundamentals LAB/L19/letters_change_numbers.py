strings = list(map(str, input().split()))
strings = [str for str in strings if str != '']
alphabet_string = 'abcdefghijklmnopqrstuvwxyz'
total_sum = 0
for current_string in strings:
    in_front_char = current_string[0]
    number = float(current_string[1:-1])
    after_char = current_string[-1]
    current_result = 0
    in_front_char_pos = 0
    after_char_pos = 0
    for index in range(len(alphabet_string)):
        if alphabet_string[index] == in_front_char.lower():
            in_front_char_pos = index + 1
            break
    for index in range(len(alphabet_string)):
        if alphabet_string[index] == after_char.lower():
            after_char_pos = index + 1
            break

    if in_front_char.isupper():
        current_result += (number / in_front_char_pos)
    if in_front_char.islower():
        current_result += (number * in_front_char_pos)
    if after_char.isupper():
        current_result -= after_char_pos
    if after_char.islower():
        current_result += after_char_pos
    total_sum += current_result
print(f'{total_sum:.2f}')