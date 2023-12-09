text = input()
new_string = ''
for symbol in text:
    if len(new_string) == 0:
        new_string += symbol
    else:
        if symbol != new_string[-1]:
            new_string += symbol
print(new_string)