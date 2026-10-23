students = []


def create_student():
    student_id = input("Enter student ID: ").strip()

    if not student_id:
        print("Student ID cannot be empty.")
        return

    # Check for duplicate student ID
    for student in students:
        if student["id"] == student_id:
            print("Error: Student ID already exists.")
            return

    name = input("Enter student name: ").strip()

    if not name:
        print("Student name cannot be empty.")
        return

    students.append({
        "id": student_id,
        "name": name
    })

    print("Student record created successfully.")


def list_students():
    if not students:
        print("No student records available.")
        return

    print("\n--- Student Records ---")

    for student in students:
        print(
            f"ID: {student['id']} | "
            f"Name: {student['name']}"
        )


def search_student():
    student_id = input("Enter student ID to search: ").strip()

    if not student_id:
        print("Student ID cannot be empty.")
        return

    for student in students:
        if student["id"] == student_id:
            print("Student found!")
            print("ID:", student["id"])
            print("Name:", student["name"])
            return

    print("Student record not found.")


def delete_student():
    student_id = input("Enter student ID to delete: ").strip()

    if not student_id:
        print("Student ID cannot be empty.")
        return

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            print("Student record deleted successfully.")
            return

    print("Student record not found.")


def main():
    while True:
        print("\n=== Student Record Manager ===")
        print("1. Create student")
        print("2. List students")
        print("3. Search student")
        print("4. Delete student")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            create_student()

        elif choice == "2":
            list_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            print("Thank you! Program closed.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()