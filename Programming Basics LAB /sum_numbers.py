BASE_NUMBER = int(input())
sum_numbers = 0  # without BASE_NUMBER

while True:
    current_number = int(input())
    sum_numbers += current_number
    if sum_numbers >= BASE_NUMBER:
        print(sum_numbers)
        break
