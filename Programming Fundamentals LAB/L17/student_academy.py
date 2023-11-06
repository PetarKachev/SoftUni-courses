number_of_students = int(input())

dictionary_with_all_results = {}

for i in range(number_of_students):
    name_of_student = input()
    grade = str(input())

    if name_of_student not in dictionary_with_all_results.keys():
        dictionary_with_all_results[name_of_student] = grade
        continue
    dictionary_with_all_results[name_of_student] += f' {grade}'

for key, value in dictionary_with_all_results.items():
    splitted_value = value.split(" ")
    splitted_value_float = [float(value) for value in splitted_value]
    current_len_list = len(splitted_value)

    sum_of_all_grades = 0
    for grade in range(len(splitted_value_float)):
        sum_of_all_grades += splitted_value_float[grade]

    final_result = sum_of_all_grades / current_len_list

    if final_result >= 4.50:
        print(f'{key} -> {final_result:.2f}')