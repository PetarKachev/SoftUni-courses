def add_songs(*args):
    dict_with_info = {}
    for element in args:
        if element[0] not in dict_with_info:
            dict_with_info[element[0]] = []
            for current_element in element[1]:
                dict_with_info[element[0]].append(current_element)
        else:
            for current_element in element[1]:
                dict_with_info[element[0]].append(current_element)
    result = ''
    for key, value in dict_with_info.items():
        result += f'- {key}\n'
        for current_value in value:
            result += f'{current_value}\n'
    return result