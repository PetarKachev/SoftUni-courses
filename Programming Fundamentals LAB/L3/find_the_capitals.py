string = input()

new_string = []

for letter in range(len(string)):
    if string[letter].isupper():
        new_string.append(letter)

print(new_string)