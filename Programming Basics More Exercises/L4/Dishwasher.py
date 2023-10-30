bottles_detergent = int(input())
dish_counter = 0
pot_counter = 0
no_more_left = False

mliters_detergent = 750 * bottles_detergent

pot_timer_counter = 0

input_line = input()
while input_line != 'End':
    items_to_wash = int(input_line)

    if pot_timer_counter == 2:
        current_detergent_used = items_to_wash * 15
        mliters_detergent -= current_detergent_used
        pot_counter += items_to_wash
        pot_timer_counter = 0

        if mliters_detergent < 0:
            no_more_left = True
            break

        input_line = input()
        continue

    current_detergent_used = items_to_wash * 5          # dishes
    mliters_detergent -= current_detergent_used
    dish_counter += items_to_wash
    pot_timer_counter += 1

    if mliters_detergent < 0:
        no_more_left = True
        break

    input_line = input()
else:
    print(f"Detergent was enough!")
    print(f"{dish_counter} dishes and {pot_counter} pots were washed.")
    print(f"Leftover detergent {mliters_detergent} ml.")

if no_more_left:
    diff = abs(mliters_detergent)
    print(f"Not enough detergent, {diff} ml. more necessary!")
