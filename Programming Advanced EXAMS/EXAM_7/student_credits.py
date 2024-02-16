def students_credits(*args):
    dict_with_courses = {}
    for element in args:
        element = element.split("-")
        dict_with_courses[element[0]] = (float(element[3]) / float(element[2])) * float(element[1])
    sum_for_diploma = sum(dict_with_courses.values())
    sorted_dict = dict(sorted(dict_with_courses.items(), key=lambda kvp: -kvp[1]))
    result = ''
    for key, value in sorted_dict.items():
        result += f"{key} - {value:.1f}\n"
    if sum_for_diploma >= 240:
        return f"Diyan gets a diploma with {sum_for_diploma:.1f} credits.\n{result}"
    else:
        return f"Diyan needs {240 - sum_for_diploma:.1f} credits more for a diploma.\n{result}"