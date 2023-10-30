days = int(input())
hours_per_day = int(input())

total_price = 0

for day in range(1, days + 1):
    current_day_sum = 0
    for hour in range(1, hours_per_day + 1):
        if day % 2 == 0 and hour % 2 == 1:
            current_day_sum += 2.50
        elif day % 2 == 1 and hour % 2 == 0:
            current_day_sum += 1.25
        else:
            current_day_sum += 1

    total_price += current_day_sum
    print(f"Day: {day} - {current_day_sum:.2f} leva")
print(f"Total: {total_price:.2f} leva")
