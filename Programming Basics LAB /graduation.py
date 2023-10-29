student_name = input()
year = 0
grades_counter = 0
failed_years = 0

while True:
    annual_grade = float(input())

    if annual_grade < 4:
        failed_years += 1

        if failed_years > 1:
            current_year = year + 1
            print(f"{student_name} has been excluded at {current_year} grade")
            break

        continue

    else:
        grades_counter += annual_grade
        year += 1

    if year == 12:
        avg_grade = grades_counter / 12
        print(f"{student_name} graduated. Average grade: {avg_grade:.2f}")
        break
