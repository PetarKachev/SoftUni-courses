first_entry = int(input())
second_entry = int(input())
diff_first = int(input())
diff_second = int(input())

first_end = first_entry + diff_first
second_end = second_entry + diff_second

for first in range(first_entry, first_end + 1):
    for second in range(second_entry, second_end + 1):

        prime_count_1 = 0
        for i in range(1, first + 1):
            if first % i == 0:
                prime_count_1 += 1

        prime_count_2 = 0
        for j in range(1, second + 1):
            if second % j == 0:
                prime_count_2 += 1

        if prime_count_1 == 2 and prime_count_2 == 2:
            print(f"{first}{second}")
