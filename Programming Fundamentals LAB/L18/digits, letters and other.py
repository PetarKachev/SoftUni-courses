string = input()

numbers = ''
letters = ''
symbols = ''

for element in range(len(string)):
    if string[element].isdigit():
        numbers += string[element]
    elif string[element].isalpha():
        letters += string[element]
    else:
        symbols += string[element]

print(numbers)
print(letters)
print(symbols)