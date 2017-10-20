students = []


def get_student_titlecase():
    student_title = []
    for student in students:
        student_titlecase  = students()
    return student_title


def print_student_title():
    student_titlecase = get_student_titlecase()

    print(student_titlecase)


def add_student(student_name, student_id):
    student = {"name": student_name, "student_id": student_id}
    students.append(student)

student_list = get_student_titlecase()

print("Done")

student_name  = input("Enter your name :")
student_id  = input("Enter your id :")
