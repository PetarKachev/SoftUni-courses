def start_spring(**kwargs):
    dict_with_types = {}
    for key, value in kwargs.items():
        if value not in dict_with_types:
            dict_with_types[value] = []
        dict_with_types[value].append(key)
        dict_with_types[value] = sorted(dict_with_types[value])

    sorted_dict = dict(sorted(dict_with_types.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])))
    result = ''

    for key, value in sorted_dict.items():
        result += f'{key}:\n'
        for nested_value in value:
            result += f'-{nested_value}\n'
    return result