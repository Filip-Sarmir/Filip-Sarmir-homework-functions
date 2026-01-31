##definition of the lists

students = []
teachers = []
homeroom_teachers = []
classes = []

student = ("Maximus", "Decimus", "2B")
students.append(student)

teacher = ("Napoleon", "Bonaparte", "Strategy and Tactics", ["1A", "2A", "3A"] )
teachers.append(teacher)

homeroom_teacher = ("Darth", "Vader", "4B")
homeroom_teachers.append(homeroom_teacher)


classes.append("2B")
classes.append("1A")
classes.append("2A")
classes.append("3A")
classes.append("4B")

## definition of the functions

def student(name, surname, class_name):
    students.append((name, surname, class_name))

def teacher(name, surname, subject, class_list):
    teachers.append((name, surname, subject, class_list))

def homeroom_teacher(name, surname, class_name):
    homeroom_teachers.append((name, surname, class_name))


while True:
    choice = input("Choose to create: student, teacher, homeroom teacher, end ")

    if choice == "student":
        name = input("Enter student name: ")
        surname = input("Enter student surname: ")
        class_name = input("Enter student class name: ")
        student(name, surname, class_name)


    elif choice == "teacher":
        name = input("Enter teacher name: ")
        surname = input("Enter teacher surname: ")
        subject = input("Enter teacher subject: ")
        class_name = input("Enter class: ")
        teacher(name, surname, subject, class_name)

    elif choice == "homeroom teacher":
        name = input("Enter homeroom teacher name: ")
        surname = input("Enter homeroom teacher surname: ")
        class_name = input("Enter class they lead: ")
        homeroom_teacher(name, surname, class_name)

    elif choice == "end":
        print("End")
        break

    elif choice == "show":
        print("Students:", students)
        print("Teachers:", teachers)
        print("Homeroom Teachers:", homeroom_teachers)
        print("Classes:", classes)









