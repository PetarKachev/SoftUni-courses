vacation_price = float(input())
balance = float(input())
spend_days_counter = 0
days = 0

while True:
    action = input()
    amount = float(input())
    days += 1

    if action == 'save':
        balance += amount
        spend_days_counter = 0
        if balance >= vacation_price:
            print(f"You saved the money for {days} days.")
            break

    if action == 'spend':
        balance -= amount
        spend_days_counter += 1
        if balance < 0:
            balance = 0
        if spend_days_counter == 5:
            print(f"You can't save the money.")
            print(days)
            break

