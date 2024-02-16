def shopping_cart(*args):
    dict_with_products = {"Soup": [], "Pizza": [], "Dessert": []}
    for element in args:
        if element == "Stop":
            break
        elif element[0] == "Soup":
            if len(dict_with_products["Soup"]) < 3:
                if element[1] not in dict_with_products["Soup"]:
                    dict_with_products["Soup"].append(element[1])
        elif element[0] == "Pizza":
            if len(dict_with_products["Pizza"]) < 4:
                if element[1] not in dict_with_products["Pizza"]:
                    dict_with_products["Pizza"].append(element[1])
        elif element[0] == "Dessert":
            if len(dict_with_products["Dessert"]) < 2:
                if element[1] not in dict_with_products["Dessert"]:
                    dict_with_products["Dessert"].append(element[1])
    dict_with_products["Soup"] = sorted(dict_with_products["Soup"])
    dict_with_products["Pizza"] = sorted(dict_with_products["Pizza"])
    dict_with_products["Dessert"] = sorted(dict_with_products["Dessert"])

    sorted_dict = dict(sorted(dict_with_products.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])))
    result = ''
    if len(dict_with_products["Soup"]) == 0 and len(dict_with_products["Pizza"]) == 0 and len(dict_with_products["Dessert"]) == 0:
        return "No products in the cart!"
    else:
        for key, value in sorted_dict.items():
            result += f'{key}:\n'
            for current_value in value:
                result += f' - {current_value}\n'
        return result