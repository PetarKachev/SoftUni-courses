number = int(input())

def calculate(num):
    if num == 100:
        print(f'100% Complete!\n[%%%%%%%%%%]')
    else:
        print(f'{num}% [{int(num // 10) * "%"}{int(10 - (num // 10)) * "."}]\nStill loading...')

calculate(number)