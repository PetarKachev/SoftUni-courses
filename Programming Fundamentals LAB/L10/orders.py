product = input()
number_of_products = int(input())

def calculate(product_name, number):
    if product_name == "coffee":
        return f'{number * 1.50:.2f}'
    elif product_name == "water":
        return f'{number * 1.00:.2f}'
    elif product_name == "coke":
        return f'{number * 1.40:.2f}'
    elif product_name == "snacks":
        return f'{number * 2.00:.2f}'

print(calculate(product, number_of_products))