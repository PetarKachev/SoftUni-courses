number = int(input())

for first in range(number):
    for second in range(number):
        for third in range(number):
            print(f'{chr(97 + first)}{chr(97 + second)}{chr(97 + third)}')