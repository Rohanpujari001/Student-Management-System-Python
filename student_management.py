
# ==========================================
#       STUDENT MANAGEMENT SYSTEM
# ==========================================

import csv
import os

FILE_NAME = "students.csv"


# 1. CREATE CSV FILE
def create_file():

    if not os.path.exists(FILE_NAME):

        with open(FILE_NAME, "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow(["Roll Number", "Name", "Marks"])

        print("Student CSV file created successfully!")


# 2. ADD STUDENT
def add_student():

    print("\n========== ADD STUDENT ==========")

    roll = input("Enter Roll Number: ").strip()
    name = input("Enter Student Name: ").strip()

    try:
        marks = float(input("Enter Student Marks: "))

        if not roll or not name:
            print("Roll Number and Name cannot be empty!")
            return

        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100!")
            return

        students = read_students()

        for student in students:

            if student["Roll Number"] == roll:
                print("Student with this Roll Number already exists!")
                return

        with open(FILE_NAME, "a", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([roll, name, marks])

        print("\nStudent Added Successfully!")

    except ValueError:
        print("Invalid Marks! Please enter a number.")


# 3. READ STUDENT DATA
def read_students():

    students = []

    try:
        with open(FILE_NAME, "r", newline="") as file:

            reader = csv.DictReader(file)

            for student in reader:
                students.append(student)

    except FileNotFoundError:
        print("Student file not found!")

    return students


# 4. VIEW ALL STUDENTS
def view_students():

    print("\n========== ALL STUDENTS ==========")

    students = read_students()

    if not students:
        print("No Student Records Found!")
        return

    print("-" * 55)

    print("{:<15} {:<20} {:<10}".format(
        "Roll Number", "Name", "Marks"
    ))

    print("-" * 55)

    for student in students:

        print("{:<15} {:<20} {:<10}".format(
            student["Roll Number"],
            student["Name"],
            student["Marks"]
        ))

    print("-" * 55)


# 5. SEARCH STUDENT
def search_student():

    print("\n========== SEARCH STUDENT ==========")

    roll = input("Enter Roll Number to Search: ").strip()

    students = read_students()

    for student in students:

        if student["Roll Number"] == roll:

            print("\nStudent Found!")

            print("Roll Number:", student["Roll Number"])
            print("Name:", student["Name"])
            print("Marks:", student["Marks"])

            return

    print("Student Not Found!")


# 6. UPDATE STUDENT
def update_student():

    print("\n========== UPDATE STUDENT ==========")

    roll = input("Enter Roll Number to Update: ").strip()

    students = read_students()

    for student in students:

        if student["Roll Number"] == roll:

            print("Current Name:", student["Name"])
            print("Current Marks:", student["Marks"])

            new_name = input("Enter New Name: ").strip()

            try:
                new_marks = float(input("Enter New Marks: "))

                if not new_name:
                    print("Name cannot be empty!")
                    return

                if new_marks < 0 or new_marks > 100:
                    print("Marks must be between 0 and 100!")
                    return

                student["Name"] = new_name
                student["Marks"] = str(new_marks)

                save_students(students)

                print("\nStudent Updated Successfully!")

            except ValueError:
                print("Invalid Marks! Please enter a number.")

            return

    print("Student Not Found!")


# 7. DELETE STUDENT
def delete_student():

    print("\n========== DELETE STUDENT ==========")

    roll = input("Enter Roll Number to Delete: ").strip()

    students = read_students()

    for student in students:

        if student["Roll Number"] == roll:

            students.remove(student)

            save_students(students)

            print("\nStudent Deleted Successfully!")

            return

    print("Student Not Found!")


# 8. SAVE STUDENT DATA
def save_students(students):

    with open(FILE_NAME, "w", newline="") as file:

        fieldnames = ["Roll Number", "Name", "Marks"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        writer.writerows(students)


# 9. MAIN MENU
def main():

    create_file()

    while True:

        print("\n====================================")
        print("       STUDENT MANAGEMENT SYSTEM")
        print("====================================")

        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("\nEnter Your Choice (1-6): ")

        if choice == "1":

            add_student()

        elif choice == "2":

            view_students()

        elif choice == "3":

            search_student()

        elif choice == "4":

            update_student()

        elif choice == "5":

            delete_student()

        elif choice == "6":

            print("\nThank You for Using Student Management System!")
            print("Program Closed Successfully!")

            break

        else:

            print("\nInvalid Choice! Please Select 1-6.")


# ==========================================
#          PROGRAM EXECUTION
# ==========================================

if __name__ == "__main__":

    main()

# ==========================================
#              END PROJECT
# ==========================================
