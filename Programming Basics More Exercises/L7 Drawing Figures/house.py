n = int(input())

roof_odd_lines = (n - 1) / 2
roof_even_lines = (n - 2) / 2
stars_roof = 0

if n % 2 == 1:   # odd roof start
    for roof_row in range(int((n + 1) / 2)):
        if roof_row == 0:
            stars_roof = 1
            print('-' * int(roof_odd_lines) + '*' * stars_roof + '-' * int(roof_odd_lines))
            stars_roof += 2
            roof_odd_lines -= 1
            continue
        print('-' * int(roof_odd_lines) + '*' * stars_roof + '-' * int(roof_odd_lines))
        stars_roof += 2
        roof_odd_lines -= 1
else:   # even roof start
    for roof_row in range(int((n + 1) / 2)):
        if roof_row == 0:
            stars_roof = 2
            print('-' * int(roof_even_lines) + '*' * stars_roof + '-' * int(roof_even_lines))
            stars_roof += 2
            roof_even_lines -= 1
            continue
        print('-' * int(roof_even_lines) + '*' * stars_roof + '-' * int(roof_even_lines))
        stars_roof += 2
        roof_even_lines -= 1

for foundation_row in range(n - int((n + 1) / 2)):
    print('|' + '*' * (n - 2) + '|')
