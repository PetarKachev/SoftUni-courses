import sys

n = int(input())
max_num = -sys.maxsize
total_sum = 0

for _ in range(n):
    current_number = int(input())
    total_sum += current_number
    if current_number > max_num:
        max_num = current_number

total_sum = total_sum - max_num

if total_sum == max_num:
    print('Yes')
    print(f"Sum = {max_num}")
else:
    diff = abs(total_sum - max_num)
    print('No')
    print(f"Diff = {diff}")