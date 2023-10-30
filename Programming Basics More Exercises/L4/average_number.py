n = int(input())
numbers_sum = 0
numbers_counter = 0

for _ in range(n):
    number = int(input())
    numbers_sum += number
    numbers_counter += 1

avg_number_sum = numbers_sum / numbers_counter

print(f"{avg_number_sum:.2f}")