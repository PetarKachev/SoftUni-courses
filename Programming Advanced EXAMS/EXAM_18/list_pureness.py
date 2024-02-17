def best_list_pureness(*args):
    import sys
    max_num = -sys.maxsize
    max_rotation = 0
    from collections import deque
    current_list = args[0]
    k = int(args[1])
    rotations = 0

    while rotations <= k:
        current_sum = 0
        for index in range(len(current_list)):
            current_sum += current_list[index] * index
        if current_sum > max_num:
            max_num = current_sum
            max_rotation = rotations
        rotations += 1

        current_list = deque(current_list)
        current_list.insert(0, current_list.pop())

    return f"Best pureness {max_num} after {max_rotation} rotations"