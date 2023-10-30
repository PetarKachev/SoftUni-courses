number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())

max_number = 0
highest_attendance = 0

for i in range(number_of_students):
    attendance_of_each_student = int(input())

    current_student_bonus = (attendance_of_each_student / number_of_lectures) * (5 + additional_bonus)

    if current_student_bonus > max_number:
        max_number = current_student_bonus
        highest_attendance = attendance_of_each_student

print(f"Max Bonus: {round(max_number)}.")
print(f"The student has attended {highest_attendance} lectures.")