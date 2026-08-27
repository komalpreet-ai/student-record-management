print("STUDENT RECORD MANAGEMENT")

students = {}


def add_student():
    roll_no = input("Enter roll number: ")
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))

    students[roll_no] = {
        "name": name,
        "marks": marks
    }

    print("Student added successfully!")


def view_students():
    if len(students) == 0:
        print("No student records found.")
    else:
        print("\nStudent Records:")

        for roll_no, student in students.items():
            print("Roll No:", roll_no)
            print("Name:", student["name"])
            print("Marks:", student["marks"])
            print("----------------")


def search_student():
    roll_no = input("Enter roll number to search: ")

    if roll_no in students:
        student = students[roll_no]
        print("Name:", student["name"])
        print("Marks:", student["marks"])
    else:
        print("Student not found.")


def delete_student():
    roll_no = input("Enter roll number to delete: ")

    if roll_no in students:
        del students[roll_no]
        print("Student deleted successfully!")
    else:
        print("Student not found.")


while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")