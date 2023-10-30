game_moves = int(input())

score = 0

zero_nine_counter = 0
ten_nineteen_counter = 0
twenty_twenty_nine_counter = 0
thirty_thirty_nine_counter = 0
forty_fifty_counter = 0
invalid_numbers_counter = 0


for _ in range(game_moves):
    current_number = int(input())

    if current_number > 50 or current_number < 0:
        score /= 2
        invalid_numbers_counter += 1
        continue

    if 0 <= current_number <= 9:
        score += (current_number * 0.20)
        zero_nine_counter += 1
    elif 10 <= current_number <= 19:
        score += (current_number * 0.30)
        ten_nineteen_counter += 1
    elif 20 <= current_number <= 29:
        score += (current_number * 0.40)
        twenty_twenty_nine_counter += 1
    elif 30 <= current_number <= 39:
        score += 50
        thirty_thirty_nine_counter += 1
    elif 40 <= current_number <= 50:
        score += 100
        forty_fifty_counter += 1

zero_nine_percent = zero_nine_counter / game_moves * 100
ten_nineteen_percent = ten_nineteen_counter / game_moves * 100
twenty_twenty_nine_percent = twenty_twenty_nine_counter / game_moves * 100
thirty_thirty_nine_percent = thirty_thirty_nine_counter / game_moves * 100
forty_fifty_percent = forty_fifty_counter / game_moves * 100
invalid_numbers_percent = invalid_numbers_counter / game_moves * 100

print(f"{score:.2f}")
print(f"From 0 to 9: {zero_nine_percent:.2f}%")
print(f"From 10 to 19: {ten_nineteen_percent:.2f}%")
print(f"From 20 to 29: {twenty_twenty_nine_percent:.2f}%")
print(f"From 30 to 39: {thirty_thirty_nine_percent:.2f}%")
print(f"From 40 to 50: {forty_fifty_percent:.2f}%")
print(f"Invalid numbers: {invalid_numbers_percent:.2f}%")
