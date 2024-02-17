dict_with_words = {}
import re
regex = r'(\w+)'
first_file = open("words.txt", "r")

for current_file in first_file:
    for nested_file in current_file.split():
        if nested_file not in dict_with_words:
            dict_with_words[nested_file] = 0

second_file = open("input.txt", "r")

for file in second_file:
    for nested_file in file.split(" "):
        word = re.findall(regex, nested_file)
        if str(word[0]).lower() in dict_with_words.keys():
            dict_with_words[str(word[0]).lower()] += 1

sorted_dict = sorted(dict_with_words.items(), key=lambda kvp: -kvp[1])
for element in sorted_dict:
    print(f'{element[0]} - {element[1]}')