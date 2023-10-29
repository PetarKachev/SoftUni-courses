n = int(input())
first_sum = 0
sec_sum = 0

for _ in range(n):
    a = int(input())
    first_sum += a

for _ in range(n):
    b = int(input())
    sec_sum += b

diff = abs(first_sum - sec_sum)

if first_sum == sec_sum:
    print(f"Yes, sum = {first_sum}")
else:
    print(f"No, diff = {diff}")
