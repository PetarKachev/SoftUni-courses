clothes_box = list(map(int, input().split()))
one_rack = int(input())
number_of_used_racks = 0
current_rack_capacity = 0

while len(clothes_box) > 0:
    if current_rack_capacity == 16:
        number_of_used_racks += 1
        current_rack_capacity = 0
    if current_rack_capacity + clothes_box[-1] <= one_rack:
        if len(clothes_box) == 1:
            current_rack_capacity += clothes_box.pop()
            number_of_used_racks += 1
        else:
            current_rack_capacity += clothes_box.pop()
    else:
        number_of_used_racks += 1
        current_rack_capacity = 0
print(number_of_used_racks)