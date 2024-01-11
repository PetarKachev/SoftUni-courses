n = int(input())

dict_student_info = {}

for i in range(n):
    name, grade = input().split(" ")
    if name not in dict_student_info.keys():
        dict_student_info[name] = []
        dict_student_info[name].append(float(grade))
    else:
        dict_student_info[name].append(float(grade))

for key, value in dict_student_info.items():
    grades = []
    for current_value in value:
        current_value = f'{current_value:.2f}'
        grades.append(str(current_value))
    average_value = sum(value) / len(value)
    print(f"{key} -> {' '.join(grades)} (avg: {average_value:.2f})")