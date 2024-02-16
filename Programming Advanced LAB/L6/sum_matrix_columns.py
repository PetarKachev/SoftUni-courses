matrix_size = list(map(int, input().split(", ")))
rows = matrix_size[0]
columns = matrix_size[1]
dict_with_sums = {}

for row in range(rows):
    data = list(map(int, input().split(" ")))
    for index in range(len(data)):
        if index not in dict_with_sums.keys():
            dict_with_sums[index] = 0
        dict_with_sums[index] += data[index]

for value in dict_with_sums.values():
    print(value)