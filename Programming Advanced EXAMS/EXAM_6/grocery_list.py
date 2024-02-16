def shop_from_grocery_list(budget, grocery_list, *args):
    bought_products = []
    for product in args:
        if product[0] in grocery_list:
            if product[0] not in bought_products:
                if budget >= product[1]:
                    bought_products.append(product[0])
                    budget -= product[1]
                else:
                    break
    missing_products = [product for product in grocery_list if product not in bought_products]
    if len(missing_products) == 0:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        return f"You did not buy all the products. Missing products: {', '.join(missing_products)}."