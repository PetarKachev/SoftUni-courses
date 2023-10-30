string = input()
word_counter = 0
string_lower = string.lower()

for i in range(len(string_lower)):
    if string_lower[i] == "f" and i + 3 <= len(string_lower):
        if string_lower[i + 1] == "i" and string_lower[i + 2] == "s" and string_lower[i + 3] == "h":
            word_counter += 1
    if string_lower[i] == "s" and i + 3 <= len(string_lower):
        if string_lower[i + 1] == "a" and string_lower[i + 2] == "n" and string_lower[i + 3] == "d":
            word_counter += 1
    if string_lower[i] == "w" and i + 4 <= len(string_lower):
        if string_lower[i + 1] == "a" and string_lower[i + 2] == "t" and string_lower[i + 3] == "e" and string_lower[i + 4] == "r":
            word_counter += 1
    if string_lower[i] == "s" and i + 2 <= len(string_lower):
        if string_lower[i + 1] == "u" and string_lower[i + 2] == "n":
            word_counter += 1

print(word_counter)


