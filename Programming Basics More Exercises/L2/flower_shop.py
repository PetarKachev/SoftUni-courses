from math import ceil, floor

magnolia_count = int(input())
zumbul_count = int(input())
rose_count = int(input())
cactus_count = int(input())
gift_price = float(input())

income = (magnolia_count * 3.25) + (zumbul_count * 4) + (rose_count * 3.50) + (cactus_count * 8)
income_after_tax = income * 0.95
diff = abs(income_after_tax - gift_price)

if income_after_tax >= gift_price:
    print(f"She is left with {floor(diff)} leva.")
else:
    print(f"She will have to borrow {ceil(diff)} leva.")