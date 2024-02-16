rows = int(input())
main_diagonal = []
secondary_diagonal = []
matrix = []
index = 0

for i in range(rows):
    data = list(map(int, input().split(" ")))
    matrix.append(data)
    main_diagonal.append(data[i])
    index = i

for element in matrix:
    secondary_diagonal.append(element[index])
    index -= 1

result = abs(sum(main_diagonal) - sum(secondary_diagonal))
print(result)