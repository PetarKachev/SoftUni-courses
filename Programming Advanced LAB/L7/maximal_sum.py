import sys
info = list(map(int, input().split(" ")))
rows = info[0]
columns = info[1]
matrix = []
max_num = -sys.maxsize

for row in range(rows):
    data = list(map(int, input().split(" ")))
    matrix.append(data)

for row in range(rows):
    if row + 2 == rows:
        break
    for col in range(columns):
        if col + 2 == columns:
            break
        first_num = matrix[row][col]
        second_num = matrix[row + 1][col]
        third_num = matrix[row + 2][col]

        forth_num = matrix[row][col + 1]
        fifth_num = matrix[row + 1][col + 1]
        sixth_num = matrix[row + 2][col + 1]

        seventh_num = matrix[row][col + 2]
        eight_num = matrix[row + 1][col + 2]
        ninth_num = matrix[row + 2][col + 2]

        current_sum = first_num + second_num + third_num + forth_num + fifth_num + sixth_num + seventh_num + eight_num + ninth_num
        if current_sum > max_num:
            max_num = current_sum
            current_combination = [[first_num, forth_num, seventh_num], [second_num, fifth_num, eight_num], [third_num, sixth_num, ninth_num]]

print(f'Sum = {max_num}')
for current_element in range(len(current_combination)):
    print(current_combination[current_element][0], current_combination[current_element][1], current_combination[current_element][2])
