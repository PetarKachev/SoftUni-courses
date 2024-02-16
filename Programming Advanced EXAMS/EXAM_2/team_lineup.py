def team_lineup(*args):
    dict_with_names = {}
    for element in args:
        if element[1] not in dict_with_names:
            dict_with_names[element[1]] = []
            dict_with_names[element[1]].append(element[0])
        else:
            dict_with_names[element[1]].append(element[0])

    sorted_dict = dict(sorted(dict_with_names.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])))
    result = ''
    for key, value in sorted_dict.items():
        result += f'{key}:\n'
        for element in value:
            result += f'  -{element}\n'
    return result