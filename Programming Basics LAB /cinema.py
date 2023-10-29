type_movie = input()
rows = int(input())
columns = int(input())
price = 0

cinema_capacity = rows * columns

if type_movie == 'Premiere':
    price = 12.00
elif type_movie == 'Normal':
    price = 7.50
elif type_movie == 'Discount':
    price = 5.00


print(f'{(cinema_capacity * price):.2f} leva')
