rows = int(input())
matrix = []
alive_cells = 0
sum_alive_cells = 0
for row in range(rows):
    data = list(map(int, input().split(" ")))
    matrix.append(data)

coordinates = list(map(str, input().split(" ")))

for coordinate in coordinates:
    coordinate = coordinate.split(",")
    row_index = int(coordinate[0])
    column_index = int(coordinate[1])

    bomb_value = int(matrix[row_index][column_index])
    if bomb_value <= 0:
        break
    matrix[row_index][column_index] = 0

    first_num = [row_index - 1, column_index - 1]
    second_num = [row_index - 1, column_index]
    third_num = [row_index - 1, column_index + 1]

    forth_num = [row_index, column_index - 1]
    fifth_num = [row_index, column_index + 1]

    sixth_num = [row_index + 1, column_index - 1]
    seventh_num = [row_index + 1, column_index]
    eight_num = [row_index + 1, column_index + 1]

    len_matrix = len(matrix)
    len_columns = len(matrix[0])

    if first_num[0] < len_matrix and first_num[1] < len_columns and matrix[first_num[0]][first_num[1]] > 0:
        if f'{first_num[0],first_num[1]}' not in coordinates and first_num[0] >= 0 and first_num[1] >= 0:
            matrix[first_num[0]][first_num[1]] -= bomb_value

    if second_num[0] < len_matrix and second_num[1] < len_columns and matrix[second_num[0]][second_num[1]] > 0:
        if f'{second_num[0], second_num[1]}' not in coordinates and second_num[0] >= 0 and second_num[1] >= 0:
            matrix[second_num[0]][second_num[1]] -= bomb_value

    if third_num[0] < len_matrix and third_num[1] < len_columns and matrix[third_num[0]][third_num[1]] > 0:
        if f'{third_num[0], third_num[1]}' not in coordinates and third_num[0] >= 0 and third_num[1] >= 0:
            matrix[third_num[0]][third_num[1]] -= bomb_value

    if forth_num[0] < len_matrix and forth_num[1] < len_columns and matrix[forth_num[0]][forth_num[1]] > 0:
        if f'{forth_num[0], forth_num[1]}' not in coordinates and forth_num[0] >= 0 and forth_num[1] >= 0:
            matrix[forth_num[0]][forth_num[1]] -= bomb_value

    if fifth_num[0] < len_matrix and fifth_num[1] < len_columns and matrix[fifth_num[0]][fifth_num[1]] > 0:
        if f'{fifth_num[0], fifth_num[1]}' not in coordinates and fifth_num[0] >= 0 and fifth_num[1] >= 0:
            matrix[fifth_num[0]][fifth_num[1]] -= bomb_value

    if sixth_num[0] < len_matrix and sixth_num[1] < len_columns and matrix[sixth_num[0]][sixth_num[1]] > 0:
        if f'{sixth_num[0], sixth_num[1]}' not in coordinates and sixth_num[0] >= 0 and sixth_num[1] >= 0:
            matrix[sixth_num[0]][sixth_num[1]] -= bomb_value

    if seventh_num[0] < len_matrix and seventh_num[1] < len_columns and matrix[seventh_num[0]][seventh_num[1]] > 0:
        if f'{seventh_num[0], seventh_num[1]}' not in coordinates and seventh_num[0] >= 0 and seventh_num[1] >= 0:
            matrix[seventh_num[0]][seventh_num[1]] -= bomb_value

    if eight_num[0] < len_matrix and eight_num[1] < len_columns and matrix[eight_num[0]][eight_num[1]] > 0:
        if f'{eight_num[0], eight_num[1]}' not in coordinates and eight_num[0] >= 0 and eight_num[1] >= 0:
            matrix[eight_num[0]][eight_num[1]] -= bomb_value

for row in range(rows):
    for element in matrix[row]:
        if element > 0:
            sum_alive_cells += element
            alive_cells += 1

print(f"Alive cells: {alive_cells}")
print(f"Sum: {sum_alive_cells}")
for element in matrix:
    print(' '.join([str(el) for el in element]))