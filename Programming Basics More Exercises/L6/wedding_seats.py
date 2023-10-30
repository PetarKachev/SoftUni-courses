last_sector = input()
rows_first_sector = int(input())
seats_odd_row = int(input())

seats_even_row = seats_odd_row + 2
total_seats = 0

for sector in range(ord('A'), ord(last_sector) + 1):
    for row in range(1, rows_first_sector + 1):
        if row % 2 == 0:
            end_value = seats_even_row
        else:
            end_value = seats_odd_row

        for seat in range(1, end_value + 1):
            print(f"{chr(sector)}{row}{chr(seat + 96)}")
            total_seats += 1

    rows_first_sector += 1
print(total_seats)
