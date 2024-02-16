data = input().split(", ")

rows = int(data[0])
columns = int(data[1])
matrix = []
sum = 0

for _ in range(rows):
    elements = [int(el) for el in input().split(", ")]
    matrix.append(elements)
    for element in elements:
        sum += element

print(sum)
print(matrix)