number_of_students = int(input())

total_grades = 0

between_2_and_3 = 0
between_3_and_4 = 0
between_4_and_5 = 0
between_5_and_6 = 0


for _ in range(number_of_students):
    current_grade = float(input())
    total_grades += current_grade
    if 2 <= current_grade <= 2.99:
        between_2_and_3 += 1
    if 3 <= current_grade <= 3.99:
        between_3_and_4 += 1
    if 4 <= current_grade <= 4.99:
        between_4_and_5 += 1
    if 5 <= current_grade <= 6.00:
        between_5_and_6 += 1

top_students = between_5_and_6 / number_of_students * 100
between_4_and_5_percentage = between_4_and_5 / number_of_students * 100
between_3_and_4_percentage = between_3_and_4 / number_of_students * 100
failed_percentage = between_2_and_3 / number_of_students * 100
avg_grade = total_grades / number_of_students

print(f"Top students: {top_students:.2f}%")
print(f"Between 4.00 and 4.99: {between_4_and_5_percentage:.2f}%")
print(f"Between 3.00 and 3.99: {between_3_and_4_percentage:.2f}%")
print(f"Fail: {failed_percentage:.2f}%")
print(f"Average: {avg_grade:.2f}")