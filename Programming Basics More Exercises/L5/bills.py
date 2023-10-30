months = int(input())

electricity_bill = 0
water_bill = 0
internet_bill = 0
others_bill = 0

for _ in range(months):
    current_month_el_bill = float(input())
    electricity_bill += current_month_el_bill
    water_bill += 20
    internet_bill += 15
    others_bill += (current_month_el_bill + 15 + 20) * 1.20

avg_bills = (electricity_bill + water_bill + internet_bill + others_bill) / months

print(f"Electricity: {electricity_bill:.2f} lv")
print(f"Water: {water_bill:.2f} lv")
print(f"Internet: {internet_bill:.2f} lv")
print(f"Other: {others_bill:.2f} lv")
print(f"Average: {avg_bills:.2f} lv")
