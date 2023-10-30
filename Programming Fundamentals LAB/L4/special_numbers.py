number = int(input())

for current_number in range(1, number + 1):
    current_number_string = str(current_number)
    sum_digits = 0
    for digit in current_number_string:
        sum_digits += int(digit)
    is_special = False
    if sum_digits == 5 or sum_digits == 7 or sum_digits == 11:
        is_special = True
    print(f'{current_number} -> {is_special}')