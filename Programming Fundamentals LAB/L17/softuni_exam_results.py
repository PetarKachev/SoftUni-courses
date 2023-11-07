student_info = input()

dictionary_for_submissions = {}
dictionary_info = {}

while student_info != "exam finished":
    student_info = student_info.split("-")
    if "banned" in student_info:
        name = student_info[0]
        del dictionary_info[name]
    else:
        name = student_info[0]
        language = student_info[1]
        points = int(student_info[2])

        if language not in dictionary_for_submissions.keys():
            dictionary_for_submissions[language] = 0
        dictionary_for_submissions[language] += 1

        if name not in dictionary_info.keys():
            dictionary_info[name] = []

        if language not in dictionary_info[name]:
            dictionary_info[name].append(language)
            dictionary_info[name].append(int(points))

        elif language in dictionary_info[name]:
            if points > dictionary_info[name][1]:
                dictionary_info[name][1] = points

    student_info = input()

print(f'Results:')
for key, value in dictionary_info.items():
    print(f'{key} | {int(value[1])}')

print(f'Submissions:')

for key, value in dictionary_for_submissions.items():
    print(f'{key} - {value}')