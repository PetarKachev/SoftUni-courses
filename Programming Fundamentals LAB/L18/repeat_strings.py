strings = input().split()

final_string = ''

for element in range(len(strings)):
    final_string += strings[element] * len(strings[element])

print(final_string)