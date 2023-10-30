first_num_border = int(input())
second_num_border = int(input())
third_num_border = int(input())

for i in range(2, first_num_border + 1):
    for j in range(2, second_num_border + 1):
        for k in range(2, third_num_border + 1):
            if i % 2 == 1 or k % 2 == 1:    # Само четни числа са на първа и трета позиция,
                continue                    # и само прости на втора
            prime_counter = 0
            for y in range(1, j + 1):
                if j % y == 0:
                    prime_counter += 1
            if prime_counter == 2:
                print(f"{i} {j} {k}")
            else:
                continue
