rows = int(input())

main_diagonal = []
secondary_diagonal = []
matrix = []
index = 0

for row in range(rows):
    data = list(map(int, input().split(", ")))
    matrix.append(data)
    main_diagonal.append(data[row])
    index = row

for element in matrix:
    secondary_diagonal.append(element[index])
    index -= 1

print(f"Primary diagonal: {', '.join([str(el) for el in main_diagonal])}. Sum: {sum(main_diagonal)}")
print(f"Secondary diagonal: {', '.join([str(el) for el in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")