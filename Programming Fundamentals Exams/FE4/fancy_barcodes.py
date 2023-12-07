import re

n = int(input())
regex = r'@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+'

for i in range(n):
    text = input()
    matches = re.findall(regex, text)

    for match in matches:
        product_group = ''
        for character in match:
            if character.isdigit():
                product_group += str(character)
        if len(product_group) == 0:
            print('Product group: 00')
            break
        else:
            print(f"Product group: {product_group}")
            break
    else:
        print("Invalid barcode")