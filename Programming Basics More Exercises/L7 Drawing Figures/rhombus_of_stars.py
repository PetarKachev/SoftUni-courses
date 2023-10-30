n = int(input())

print(' ' * (n - 1) + '*')
#   upper row
for row in range(1, n):
    print(' ' * (n - row - 1) + '* ' * (row + 1))
#   first half and middle sections
for row2 in range(n, 1, - 1):
    print(' ' * (n - row2 + 1) + '* ' * (row2 - 1))
#   second half section
