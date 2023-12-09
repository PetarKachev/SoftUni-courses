strings = list(map(str, input().split(" ")))
first_string_base = strings[0]
second_string_base = strings[1]

all_sum = 0
counter = 0

if len(first_string_base) > len(second_string_base):
    first_string = first_string_base[:len(second_string_base)]
    second_string = second_string_base[:len(second_string_base)]
    whats_left = first_string_base[len(second_string_base):]

    while counter < len(first_string):
        all_sum += (ord(first_string[counter]) * ord(second_string[counter]))
        counter += 1
    for character in whats_left:
        all_sum += ord(character)


elif len(first_string_base) < len(second_string_base):
    second_string = second_string_base[:len(first_string_base)]
    first_string = first_string_base[:len(first_string_base)]
    whats_left = second_string_base[len(first_string_base):]

    while counter < len(first_string):
        all_sum += (ord(first_string[counter]) * ord(second_string[counter]))
        counter += 1
    for character in whats_left:
        all_sum += ord(character)

else:
    while counter < len(first_string_base):
        all_sum += (ord(first_string_base[counter]) * ord(second_string_base[counter]))
        counter += 1

print(all_sum)