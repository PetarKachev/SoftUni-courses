deposited_amount = float(input())
months = int(input())
annual_interest = float(input())

aquired_interest = deposited_amount * (annual_interest / 100)
monthly_rate = aquired_interest / 12
final_amount = deposited_amount + (months * monthly_rate)

print(final_amount)