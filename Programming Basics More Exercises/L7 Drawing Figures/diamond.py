n = int(input())

rear_lines = (n - 1) // 2
mid_lines = 1

if n % 2 == 1:
    for upper_row in range(n // 2 + 1):
        if upper_row == 0:
            print('-' * rear_lines + '*' + '-' * rear_lines)
            rear_lines -= 1
            continue
        print('-' * rear_lines + '*' + '-' * mid_lines + '*' + '-' * rear_lines)
        rear_lines -= 1
        mid_lines += 2
    rear_lines += 1
    mid_lines -= 2
    for lower_row in range(n - (n // 2 + 1)):
        if lower_row == n // 2 - 1:
            rear_lines += 1
            print('-' * rear_lines + '*' + '-' * rear_lines)
            continue
        rear_lines += 1
        mid_lines -= 2
        print('-' * rear_lines + '*' + '-' * mid_lines + '*' + '-' * rear_lines)
else:
    for upper_row in range(n // 2):
        if upper_row == 0:
            print('-' * rear_lines + '**' + '-' * rear_lines)
            rear_lines -= 1
            mid_lines += 1
            continue
        print('-' * rear_lines + '*' + '-' * mid_lines + '*' + '-' * rear_lines)
        rear_lines -= 1
        mid_lines += 2
    rear_lines += 1
    mid_lines -= 2
    for lower_row in range(n - (n // 2) - 1):
        rear_lines += 1
        mid_lines -= 2
        print('-' * rear_lines + '*' + '-' * mid_lines + '*' + '-' * rear_lines)