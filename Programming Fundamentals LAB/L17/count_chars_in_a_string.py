input_info = input().split(" ")
text = ''.join(input_info)

dictionary = {}

for character in text:
    if character not in dictionary:
        dictionary[character] = 0
    dictionary[character] += 1

for (key, value) in dictionary.items():
    print(f'{key} -> {value}')