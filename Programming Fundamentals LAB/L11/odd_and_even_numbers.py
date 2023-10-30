number = input()

def odd_even(num):
    even_sum = 0
    odd_sum = 0
    for i in num:
        if int(i) % 2 == 0:
            even_sum += int(i)
        elif int(i) % 2 != 0:
            odd_sum += int(i)
    return f'Odd sum = {odd_sum}, Even sum = {even_sum}'

print(odd_even(number))