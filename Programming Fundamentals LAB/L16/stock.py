products = input().split(" ")

dict_list = {}

for i in range(0, len(products), 2):
    key = products[i]
    value = products[i + 1]
    dict_list[key] = int(value)

searched_products = input().split(" ")

for item in searched_products:
    if item in dict_list:
        print(f'We have {dict_list[item]} of {item} left')
    else:
        print(f"Sorry, we don\'t have {item}")