info = list(map(int, input().split(" ")))
rows = info[0]
columns = info[1]
collected_patterns = 0
matrix = []

for row in range(rows):
    data = list(map(str, input().split(" ")))
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
        if first_num == second_num == third_num == forth_num:
            collected_patterns += 1

print(collected_patterns)