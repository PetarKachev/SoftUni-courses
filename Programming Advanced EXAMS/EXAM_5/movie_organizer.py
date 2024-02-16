def movie_organizer(*args):
    dict_names = {}
    for element in args:
        name = element[0]
        genre = element[1]
        if genre not in dict_names.keys():
            dict_names[genre] = []
        dict_names[genre].append(name)
        dict_names[genre] = sorted(dict_names[genre])
    sorted_dict = dict(sorted(dict_names.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])))
    result = ""
    for key, value in sorted_dict.items():
        result += f'{key} - {len(value)}\n'
        for nested_value in value:
            result += f'* {nested_value}\n'
    return result