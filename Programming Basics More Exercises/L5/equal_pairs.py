from sys import maxsize

n = int(input())

max_diff = -maxsize
last_sum = 0
pairs_equal_counter = 0

for i in range(n):
    first_num = int(input())
    second_num = int(input())
    current_sum = first_num + second_num

    if i == 0:
        last_sum = current_sum
        pairs_equal_counter += 1
        continue
    elif last_sum == current_sum:
        pairs_equal_counter += 1
    else:
        current_diff = abs(last_sum - current_sum)
        if current_diff > max_diff:
            max_diff = current_diff

    last_sum = current_sum

if pairs_equal_counter == n:
    print(f"Yes, value={last_sum}")
else:
    print(f"No, maxdiff={max_diff}")
