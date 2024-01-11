import sys
n = int(input())
max_num = - sys.maxsize

for i in range(n):
    ranges = input().split("-")
    first_range = ranges[0]
    second_range = ranges[1]
    first_range = first_range.split(",")
    second_range = second_range.split(",")
    first_start = int(first_range[0])
    first_end = int(first_range[1])
    second_start = int(second_range[0])
    second_end = int(second_range[1])

    if first_start < second_start < first_end and first_start < second_end < first_end:
        first_num, second_num = second_start, second_end
        current_lenght = second_num - first_num

        if current_lenght > max_num:
            max_num = current_lenght
            intersection = [element for element in range(first_num, second_num + 1)]

    elif second_start < first_start < second_end and second_start < first_end < second_end:
        first_num, second_num = first_start, first_end
        current_lenght = second_num - first_num

        if current_lenght > max_num:
            max_num = current_lenght
            intersection = [element for element in range(first_num, second_num + 1)]

    elif second_start < first_start < first_end and second_start < second_end < first_end:
        first_num, second_num = first_start, second_end
        current_lenght = second_num - first_num

        if current_lenght > max_num:
            max_num = current_lenght
            intersection = [element for element in range(first_num, second_num + 1)]

    elif first_start < second_start < second_end and first_start < first_end < second_end:
        first_num, second_num = second_start, first_end
        current_lenght = second_num - first_num

        if current_lenght > max_num:
            max_num = current_lenght
            intersection = [element for element in range(first_num, second_num + 1)]

print(f"Longest intersection is {intersection} with length {len(intersection)}")