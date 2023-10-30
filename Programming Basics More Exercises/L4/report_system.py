required_amount = int(input())

total_amount = 0

cash_amount = 0
credit_card_amount = 0

people_paid_in_cash_counter = 0
people_paid_with_card_counter = 0

cc_counter = 0

input_line = input()
while input_line != 'End':
    item_price = int(input_line)

    if item_price > 100 and cc_counter == 0:
        print("Error in transaction!")
        cc_counter = 1
        input_line = input()
        continue

    if item_price < 10 and cc_counter == 1:
        print("Error in transaction!")
        cc_counter = 0
        input_line = input()
        continue

    if cc_counter == 0:
        total_amount += item_price
        cc_counter = 1
        cash_amount += item_price
        people_paid_in_cash_counter += 1
        print("Product sold!")

        if total_amount >= required_amount:
            break

        input_line = input()
        continue

    if cc_counter == 1:
        total_amount += item_price
        cc_counter = 0
        credit_card_amount += item_price
        people_paid_with_card_counter += 1
        print("Product sold!")

        if total_amount >= required_amount:
            break

    input_line = input()

else:
    print("Failed to collect required money for charity.")

if total_amount >= required_amount:
    avg_cash = cash_amount / people_paid_in_cash_counter
    avg_cc = credit_card_amount / people_paid_with_card_counter
    print(f"Average CS: {avg_cash:.2f}")
    print(f"Average CC: {avg_cc:.2f}")
