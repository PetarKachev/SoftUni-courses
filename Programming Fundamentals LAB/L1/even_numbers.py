number = int(input())

positive_numbers = 0
all_positive_numbers = 0

for i in range(number):
    num = int(input())
    if num % 2 == 0:
        positive_numbers += 1
    else:
        print(f'{num} is odd!')
        break
    all_positive_numbers += 1

if num % 2 == 0:
    print('All numbers are even.')