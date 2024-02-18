def create(num: int):
    fibonacci_nums = []
    for num in range(0, num):

        if len(fibonacci_nums) == 0:
            fibonacci_nums.append(0)

        elif len(fibonacci_nums) == 1:
            fibonacci_nums.append(1)

        else:
            next_num = int(fibonacci_nums[-1]) + int(fibonacci_nums[-2])
            fibonacci_nums.append(next_num)

        if len(fibonacci_nums) == num:
            break

    return fibonacci_nums