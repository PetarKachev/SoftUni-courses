input_info = input()

quantity_dictionary = {}
prices_dictionary = {}

while input_info != "buy":
    input_info = input_info.split(" ")

    product = str(input_info[0])
    price = float(input_info[1])
    quantity = int(input_info[2])

    if product not in quantity_dictionary.keys():
        quantity_dictionary[product] = 0
        prices_dictionary[product] = 0.00
    quantity_dictionary[product] += quantity
    prices_dictionary[product] = price

    input_info = input()

for key, value in quantity_dictionary.items():
    price = value * prices_dictionary[key]
    print(f'{key} -> {price:.2f}')