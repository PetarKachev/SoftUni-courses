available_balance = 0

while True:
    data = input()  # text

    if data == 'NoMoreMoney':
        break

    current_number = float(data)  # We turn the text into a number

    if current_number <= 0:
        print('Invalid operation!')
        break

    available_balance += current_number
    print(f"Increase: {current_number:.2f}")

print(f"Total: {available_balance:.2f}")
