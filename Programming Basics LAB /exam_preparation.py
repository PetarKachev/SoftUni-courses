bad_grades_num = int(input())
bad_grade_counter = 0
grades_sum = 0
solved_problems = 0
last_problem = ''
enough_flag = False
failed_flag = False

while True:
    problem = input()
    if problem == 'Enough':
        enough_flag = True
        break

    grade = int(input())

    if grade <= 4:
        bad_grade_counter += 1
        if bad_grade_counter == bad_grades_num:
            failed_flag = True
            break

    grades_sum += grade
    solved_problems += 1
    last_problem = problem

if enough_flag:
    avg_grade = grades_sum / solved_problems
    print(f"Average score: {avg_grade:.2f}")
    print(f"Number of problems: {solved_problems}")
    print(f"Last problem: {last_problem}")
if failed_flag:
    print(f"You need a break, {bad_grade_counter} poor grades.")
