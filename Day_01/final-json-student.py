import json
FILE_NAME = "students.json"

def create_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))

    try:
        with open(FILE_NAME, "r") as file:
            students = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        students = []

    student = {
        "id": len(students) + 1,
        "name": name,
        "age": age
    }

    # Add student to list
    students.append(student)

    # Save students to file
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)

    print("Student created successfully!")

# ---------------- READ ----------------
def read_students():
    try:
        with open(FILE_NAME, "r") as file:
            students = json.load(file)

        if len(students) == 0:
            print("No students found.")
        else:
            for student in students:
                print(student)

    except FileNotFoundError:
        print("No student file found.")

#---------------------------------------------
def update_student():
    student_id = int(input("Enter student ID to update: "))

    try:
        with open(FILE_NAME, "r") as file:
            students = json.load(file)

        found = False

        # Find the student
        for student in students:
            if student["id"] == student_id:

                student["name"] = input("Enter new name: ")
                student["age"] = int(input("Enter new age: "))

                found = True
                break

        # Save changes
        if found:
            with open(FILE_NAME, "w") as file:
                json.dump(students, file, indent=4)

            print("Student updated successfully!")
        else:
            print("Student not found.")

    except FileNotFoundError:
        print("No student file found.")


# ---------------- DELETE ----------------
def delete_student():
    student_id = int(input("Enter student ID to delete: "))

    try:
        with open(FILE_NAME, "r") as file:
            students = json.load(file)

        for student in students:
            if student["id"] == student_id:
                students.remove(student)

                with open(FILE_NAME, "w") as file:
                    json.dump(students, file, indent=4)

                print("Student deleted successfully!")
                return

        print("Student not found.")

    except FileNotFoundError:
        print("No student file found.")


# ---------------- MENU ----------------
while True:
    print("\n--- Student CRUD Menu ---")
    print("1. Create Student")
    print("2. Read Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_student()

    elif choice == "2":
        read_students()

    elif choice == "3":
        update_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Program ended.")
        break

    else:
        print("Invalid choice.")