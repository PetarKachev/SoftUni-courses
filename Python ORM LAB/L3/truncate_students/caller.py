import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Student


def add_students():

    Student1 = Student(
        student_id='FC5204',
        first_name='John',
        last_name='Doe',
        birth_date='1995-05-15',
        email='john.doe@university.com'
    )
    Student1.save()

    Student2 = Student(
        student_id='FE0054',
        first_name='Jane',
        last_name='Smith',
        email='jane.smith@university.com'
    )
    Student2.save()

    Student3 = Student(
        student_id='FH2014',
        first_name='Alice',
        last_name='Johnson',
        birth_date='1998-02-10',
        email='alice.johnson@university.com'
    )
    Student3.save()

    Student4 = Student(
        student_id='FH2015',
        first_name='Bob',
        last_name='Wilson',
        birth_date='1996-11-25',
        email='bob.wilson@university.com'
    )
    Student4.save()

def get_students_info():
    students = Student.objects.all()
    result = []

    for student in students:
        result.append(
            f"Student №{student.student_id}: {student.first_name} {student.last_name}; Email: {student.email}"
        )

    return '\n'.join(result)

def update_students_emails():
    students = Student.objects.all()

    for student in students:
        student_email = student.email.replace("university.com", "uni-students.com")
        student.email = student_email
        student.save()

def truncate_students():
    all_students = Student.objects.all()
    all_students.delete()

truncate_students()
print(Student.objects.all())
print(f'Number of students: {Student.objects.count()}')