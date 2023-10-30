number_of_orders = int(input())

final_price = 0

for i in range(1, number_of_orders + 1):
    price_for_current_order = 0
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed_per_days = int(input())

    if 0.01 <= price_per_capsule <= 100.00 and 1 <= days <= 31 and 1 <= capsules_needed_per_days <= 2000:
        price_for_current_order = (capsules_needed_per_days * price_per_capsule) * days
        final_price += price_for_current_order

    if price_for_current_order > 0:
        print(f"The price for the coffee is: ${price_for_current_order:.2f}")

print(f"Total: ${final_price:.2f}")