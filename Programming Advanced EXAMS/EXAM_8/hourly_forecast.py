def forecast(*args):
    sunny_dict = {}
    cloudy_dict = {}
    rainy_dict = {}
    for element in args:
        if element[1] == "Sunny":
            sunny_dict[element[0]] = "Sunny"
        elif element[1] == "Cloudy":
            cloudy_dict[element[0]] = "Cloudy"
        elif element[1] == "Rainy":
            rainy_dict[element[0]] = "Rainy"
    sorted_sunny = dict(sorted(sunny_dict.items(), key=lambda kvp: kvp[0]))
    sorted_cloudy = dict(sorted(cloudy_dict.items(), key=lambda kvp: kvp[0]))
    sorted_rainy = dict(sorted(rainy_dict.items(), key=lambda kvp: kvp[0]))
    for key, value in sorted_cloudy.items():
        sorted_sunny[key] = value
    for key, value in sorted_rainy.items():
        sorted_sunny[key] = value
    result = ''
    for key, value in sorted_sunny.items():
        result += f'{key} - {value}\n'
    return result