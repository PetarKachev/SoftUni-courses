number_of_rows = int(input())
all_lists = []
for i in range(number_of_rows):
    current_field = list(map(int, input().split(" ")))
    all_lists.append(current_field)
row_and_col = input().split(" ")
destroyed_ships = 0

for element in row_and_col:
    element = element.split("-")
    row = int(element[0])
    col = int(element[1])
    if all_lists[row][col] > 0:
        all_lists[row][col] -= 1
        if all_lists[row][col] == 0:
            destroyed_ships += 1
print(destroyed_ships)