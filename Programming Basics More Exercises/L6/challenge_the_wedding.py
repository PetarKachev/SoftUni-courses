males = int(input())
females = int(input())
available_tables = int(input())
no_more_tables = False

for male in range(1, males + 1):
    for female in range(1, females + 1):
        print(f"({male} <-> {female})", end=" ")
        available_tables -= 1
        if available_tables == 0:
            no_more_tables = True
            break
    if no_more_tables:
        break
