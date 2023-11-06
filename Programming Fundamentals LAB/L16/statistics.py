products = {}

command = input()

while command != "statistics":
    tokens = command.split(": ")
    key = tokens[0]
    value = int(tokens[1])
    if key not in products:
        products[key] = 0
    products[key] += value
    command = input()

print(f'Products in stock:')

for key, value in products.items():
    print(f'- {key}: {value}')
print(f'Total Products: {len(products.keys())}')
print(f'Total Quantity: {sum(products.values())}')
