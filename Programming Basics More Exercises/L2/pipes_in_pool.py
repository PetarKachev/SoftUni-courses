volume = int(input())
p1_debit_per_hour = int(input())
p2_debit_per_hour = int(input())
hours = float(input())

p1_filled = p1_debit_per_hour * hours
p2_filled = p2_debit_per_hour * hours
liters_in_pool = p1_filled + p2_filled

diff = abs(volume - (p1_filled + p2_filled))

pool_filled_percentage = (p1_filled + p2_filled) / volume * 100
p1_percentage = (liters_in_pool - p2_filled) / liters_in_pool * 100
p2_percentage = (liters_in_pool - p1_filled) / liters_in_pool * 100

if volume >= liters_in_pool :
    print(f"The pool is {pool_filled_percentage}% full. Pipe 1: {p1_percentage:.2f}%. Pipe 2: {p2_percentage:.2f}%.")
else:
    print(f"For {hours} hours the pool overflows with {diff} liters.")
