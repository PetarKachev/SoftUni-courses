def sorting_cheeses(**kwargs):
    sorted_dict = dict(sorted(kwargs.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])))
    result = ''
    for key, value in sorted_dict.items():
        result += f'{key}\n'
        value = sorted(value, reverse=True)
        for element in value:
            result += f'{element}\n'

    return result