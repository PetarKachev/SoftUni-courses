string = input().split("|")
string = string[::-1]
matrix = []

for element in string:
    element = element.split(' ')
    for current_el in element:
        if current_el != "":
            matrix.append(current_el)

print(' '.join(matrix))