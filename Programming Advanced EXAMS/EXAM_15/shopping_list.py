def shopping_list(budget, **kwargs):
    type_products = []
    result = ''

    if budget >= 100:
        for key, value in kwargs.items():
            price = float(value[0])
            quantity = float(value[1])

            if budget >= price * quantity:
                budget -= price * quantity
                result += f"You bought {key} for {price * quantity:.2f} leva.\n"
                if key not in type_products:
                    type_products.append(key)
                    if len(type_products) == 5:
                        break
    else:
        result += "You do not have enough budget."
    return result