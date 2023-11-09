import os
import django

from datetime import date

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Student


def add_students():
    first_student = Student(
        student_id="FC5204",
        first_name="John",
        last_name="Doe",
        birth_date="1995-05-15",
        email="john.doe@university.com"
    )
    first_student.save()

    second_student = Student(
        student_id="FE0054",
        first_name="Jane",
        last_name="Smith",
        email="jane.smith@university.com"
    )
    second_student.save()

    third_student = Student(
        student_id="FH2014",
        first_name="Alice",
        last_name="Johnson",
        birth_date="1998-02-10",
        email="alice.johnson@university.com"
    )
    third_student.save()

    fourth_student = Student(
        student_id="FH2015",
        first_name="Bob",
        last_name="Wilson",
        birth_date="1996-11-25",
        email="bob.wilson@university.com"
    )
    fourth_student.save()


add_students()
print(Student.objects.all())


def get_students_info():
    all_students_info = []

    for student in Student.objects.all():
        all_students_info.append(
            f"Student №{student.student_id}: "
            f"{student.first_name} {student.last_name}; "
            f"Email: {student.email}")

    return '\n'.join(all_students_info)


print(get_students_info())


def update_students_emails():
    for student in Student.objects.all():
        updated_email = student.email.replace("university.com", "uni-students.com")
        student.email = updated_email
        student.save()


update_students_emails()
for stud in Student.objects.all():
    print(stud.email)


def truncate_students():
    Student.objects.all().delete()


truncate_students()
print(Student.objects.all())
print(f"Number of students: {Student.objects.count()}")

# Import your models
# Create and check models
# Run and print your queries
