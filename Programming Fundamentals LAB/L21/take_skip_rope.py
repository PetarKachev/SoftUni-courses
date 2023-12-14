string = input()

numbers_list = []
non_numbers_list = []
for char in string:
    if char.isdigit():
        numbers_list.append(char)
    else:
        non_numbers_list.append(char)

take_list = []
skip_list = []

for index in range(len(numbers_list)):
    if index % 2 == 0:
        take_list.append(numbers_list[index])
    else:
        skip_list.append(numbers_list[index])

counter = 0
taken_string = []
while counter < len(take_list) and counter < len(skip_list):
    taken_part = int(take_list[counter])
    skipped_part = int(skip_list[counter])
    taken_string.append(non_numbers_list[:taken_part])
    non_numbers_list = non_numbers_list[taken_part:]
    non_numbers_list = non_numbers_list[skipped_part:]
    counter += 1

final_string = ''
for element in taken_string:
    if len(element) > 0:
        final_string += ''.join(element)
print(final_string)
