def softuni_students(*args, **kwargs):
    dict_with_students = {}
    invalid_students = []
    for element in args:
        if element[1] not in dict_with_students:
            dict_with_students[element[1]] = element[0]
    for key, value in kwargs.items():
        for nested_key, nested_value in dict_with_students.items():
            if key == nested_value:
                dict_with_students[nested_key] = value

    for key, value in dict_with_students.items():
        if value[:2] == "id":
            invalid_students.append(key)
    for element in invalid_students:
        if element in dict_with_students:
            del dict_with_students[element]
    sorted_dict = dict(sorted(dict_with_students.items(), key=lambda kvp: kvp[0]))

    result_valid = ''
    sorted_invalid = ', '.join(sorted(invalid_students))
    for key, value in sorted_dict.items():
        result_valid += f"*** A student with the username {key} has successfully finished the course {value}!\n"
    if len(invalid_students) > 0:
        result_valid += f"!!! Invalid course students: {sorted_invalid}"
    return f'{result_valid}'