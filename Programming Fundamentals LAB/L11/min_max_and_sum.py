numbers = input().split(" ")
def min_max_sum(num):
    import sys
    max_value = - sys.maxsize
    min_value = sys.maxsize
    sum_of_all_nums = 0
    for i in num:
        sum_of_all_nums += int(i)
        if int(i) < min_value:
            min_value = int(i)
        elif int(i) > max_value:
            max_value = int(i)
    print(f'The minimum number is {min_value}')
    print(f'The maximum number is {max_value}')
    print(f'The sum number is: {sum_of_all_nums}')

min_max_sum(numbers)