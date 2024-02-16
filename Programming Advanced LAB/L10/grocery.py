def grocery_store(**kwargs):
    sorted_element = sorted(kwargs.items(), key=lambda kvp: (-kvp[1], -len(kvp[0]), (kvp[0])))
    result = ''
    for element in sorted_element:
        result += f'{str(element[0])}: {str(element[1])}\n'
    return result