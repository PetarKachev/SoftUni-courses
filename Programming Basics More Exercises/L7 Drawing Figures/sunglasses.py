from math import floor
n = int(input())

spaces = ' ' * n
frame = '*' * (2 * n)
lens = '*' + '/' * ((n * 2) - 2) + '*'
connection = '|' * n

print(frame + spaces + frame)
# Top section

for row in range(n - 2):
    if row == floor((n - 1) / 2 - 1):
        print(lens + connection + lens)
    else:
        print(lens + spaces + lens)

print(frame + spaces + frame)
# Bottom section
