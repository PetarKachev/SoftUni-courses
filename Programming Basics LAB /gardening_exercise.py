square_meters_to_green = float(input())

price_for_greening = square_meters_to_green * 7.61
discount = price_for_greening * 0.18
final_price = price_for_greening - discount

print(f"The final price is: {final_price} lv.")
print(f"The discount is: {discount} lv.")