students = []

while True:

    print("\nWelcome to the Student Data Organizer!")
    print("\nSelect an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = int(input("Enter your choice: "))


    if choice == 1:

        print("\nEnter student details:")

        student_id = input("Student ID: ")
        name = input("Name: ")
        age = input("Age: ")
        grade = input("Grade: ")
        dob = input("Date of Birth (YYYY-MM-DD): ")
        subjects = input("Subjects (comma-separated): ").split(",")

        student = {
            "id": student_id,
            "name": name,
            "age": age,
            "grade": grade,
            "dob": dob,
            "subjects": subjects
        }

        students.append(student)

        print("\nStudent added successfully!")


    elif choice == 2:

        print("\n--- Display All Students ---")

        if len(students) == 0:
            print("No student records found.")
        else:
            for student in students:
                print(
                    f"Student ID: {student['id']} | "
                    f"Name: {student['name']} | "
                    f"Age: {student['age']} | "
                    f"Grade: {student['grade']} | "
                    f"Subjects: {', '.join(student['subjects'])}"
                )


    elif choice == 3:

        update_id = input("\nEnter Student ID to update: ")

        found = False

        for student in students:

            if student["id"] == update_id:

                print("\nEnter new details:")

                student["name"] = input("New Name: ")
                student["age"] = input("New Age: ")
                student["grade"] = input("New Grade: ")
                student["dob"] = input("New Date of Birth: ")
                student["subjects"] = input(
                    "New Subjects (comma-separated): "
                ).split(",")

                print("\nStudent information updated successfully!")

                found = True
                break

        if found == False:
            print("Student not found.")


    elif choice == 4:

        delete_id = input("\nEnter Student ID to delete: ")

        found = False

        for student in students:

            if student["id"] == delete_id:

                students.remove(student)

                print("\nStudent deleted successfully!")

                found = True
                break

        if found == False:
            print("Student not found.")


    elif choice == 5:

        all_subjects = []

        for student in students:

            for subject in student["subjects"]:

                subject = subject.strip()

                if subject not in all_subjects:
                    all_subjects.append(subject)

        print("\n--- Subjects Offered ---")

        if len(all_subjects) == 0:
            print("No subjects available.")
        else:
            for subject in all_subjects:
                print(subject)


    elif choice == 6:

        print("\nExiting program...")
        break

    else:
        print("\nInvalid choice. Please try again.")