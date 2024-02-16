def words_sorting(*args):
    dict_values = {}
    sum = 0
    for element in args:
        if element not in dict_values:
            dict_values[element] = 0
            for current_letter in element:
                dict_values[element] += ord(current_letter)
            sum += dict_values[element]

    result = ''
    if sum % 2 == 0:
        sorted_dict = dict(sorted(dict_values.items(), key=lambda kvp: kvp[0]))
        for key, value in sorted_dict.items():
            result += f"{key} - {value}\n"
        return result
    else:
        sorted_dict = dict(sorted(dict_values.items(), key=lambda kvp: (-kvp[1])))
        for key, value in sorted_dict.items():
            result += f"{key} - {value}\n"
        return result