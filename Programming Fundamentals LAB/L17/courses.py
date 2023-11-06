course_information = input()

course_dictionary = {}

while course_information != "end":
    course_information = course_information.split(" : ")
    the_course_name = str(course_information[0])
    first_name_of_the_person = str(course_information[1])
    name_of_the_person = f'-- {first_name_of_the_person}'

    if the_course_name not in course_dictionary.keys():
        course_dictionary[the_course_name] = name_of_the_person
    else:
        course_dictionary[the_course_name] += f'/{name_of_the_person}'

    course_information = input()

for key, value in course_dictionary.items():
    splitted_names = value.split("/")
    print(f'{key}: {len(splitted_names)}')
    print('\n'.join(splitted_names))