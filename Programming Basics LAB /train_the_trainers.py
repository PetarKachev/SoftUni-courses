judges = int(input())
grade_counter = 0
grades_sum = 0

input_line = input()
while input_line != 'Finish':
    presentation_name = input_line

    sum_current_grades = 0
    for _ in range(judges):
        current_grade = float(input())
        grade_counter += 1
        grades_sum += current_grade
        sum_current_grades += current_grade

    avg_current_grade = sum_current_grades / judges
    print(f"{presentation_name} - {avg_current_grade:.2f}.")

    input_line = input()

avg_total_grade = grades_sum / grade_counter
print(f"Student's final assessment is {avg_total_grade:.2f}.")
