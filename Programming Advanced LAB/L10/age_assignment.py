def age_assignment(*args, **kwargs):
    new_dict = {}

    for element in args:
        if element[0] in kwargs:
            new_dict[element] = kwargs[element[0]]

    sorted_dict = sorted(new_dict.items(), key=lambda kvp: (kvp[0]))
    result = ''
    for element in sorted_dict:
        result += f"{element[0]} is {element[1]} years old.\n"
    return result