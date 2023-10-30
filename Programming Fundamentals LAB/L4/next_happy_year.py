year = int(input())

while True:
    year += 1
    year_string = str(year)
    if len(year_string) == len(set(year_string)):
        break

print(year)