input_info = list(map(int, input().split(", ")))
rows = input_info[0]
columns = input_info[1]
matrix = []
sum_matrix = []
combination_matrix = []

for row in range(rows):
    data = list(map(int, input().split(", ")))
    matrix.append(data)

for row in range(rows):
    if row + 1 == rows:
        break
    for col in range(columns):
        if col + 1 == columns:
            break

        first_num = matrix[row][col]
        second_num = matrix[row + 1][col]
        third_num = matrix[row][col + 1]
        forth_num = matrix[row + 1][col + 1]
        current_sum = first_num + second_num + third_num + forth_num
        sum_matrix.append(current_sum)
        combination_matrix.append([[first_num, third_num], [second_num, forth_num]])

max_sum = max(sum_matrix)
needed_index = sum_matrix.index(max_sum)
print(' '.join(str(el) for el in combination_matrix[needed_index][0]))
print(' '.join(str(el) for el in combination_matrix[needed_index][1]))
print(max_sum)