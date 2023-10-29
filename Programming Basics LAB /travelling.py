while True:
    country_name = input()
    if country_name == 'End':
        break
    cost = float(input())
    balance = 0
    while True:
        money_saved = float(input())
        balance += money_saved
        if balance >= cost:
            print(f"Going to {country_name}!")
            break
