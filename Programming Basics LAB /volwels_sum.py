text = input()
value = 0

for i in text:
    if i == 'a':
        value += 1
    elif i == 'e':
        value += 2
    elif i == 'hour':
        value += 3
    elif i == 'o':
        value += 4
    elif i == 'u':
        value += 5
print(value)