import json

def add_student(students):
    print("\n--- Add Student ---")

    name = input("Enter student name: ")

    try:
        study_hours = float(input("Enter study hours: "))
        attendance = float(input("Enter attendance percentage: "))
        marks = float(input("Enter marks percentage: "))
        assignment = float(input("Enter assignment percentage: "))
        sleep_hours = float(input("Enter sleep hours: "))

        if not 0 <= attendance <= 100:
            print("Attendance must be between 0 and 100.")
            return

        if not 0 <= marks <= 100:
            print("Marks must be between 0 and 100.")
            return

        if not 0 <= assignment <= 100:
            print("Assignment marks must be between 0 and 100.")
            return

        student = {
            "name": name,
            "study_hours": study_hours,
            "attendance": attendance,
            "marks": marks,
            "assignment": assignment,
            "sleep_hours": sleep_hours
        }

        students.append(student)

        print("\nStudent added successfully!")

    except ValueError:
        print("\nPlease enter numbers only for study hours, attendance, marks, assignment and sleep hours.")

def calculate_performance(marks, attendance, assignment, study_hours, sleep_hours):

    study_score = min(study_hours * 10, 100)
    sleep_score = min(sleep_hours * 10, 100)

    score = (
        marks * 0.40
        + attendance * 0.20
        + assignment * 0.20
        + study_score * 0.15
        + sleep_score * 0.05
    )

    return score


def get_status(score):

    if score >= 90:
        return "Excellent"

    elif score >= 75:
        return "Good"

    elif score >= 60:
        return "Average"

    else:
        return "Needs Improvement"


def give_suggestions(study_hours, attendance, marks, assignment, sleep_hours):

    print()
    print("========== SUGGESTIONS ==========")

    if study_hours < 4:
        print("• Try to increase your study time to at least 4 hours.")

    if attendance < 75:
        print("• Improve your attendance. Try to maintain at least 75%.")

    if assignment < 60:
        print("• Focus more on your assignments.")

    if sleep_hours < 7:
        print("• Try to get at least 7 hours of sleep.")

    if marks < 60:
        print("• Focus on improving your academic marks.")

    if (
        study_hours >= 4
        and attendance >= 75
        and assignment >= 60
        and sleep_hours >= 7
        and marks >= 60
    ):
        print("• Great work! Keep maintaining your current routine.")


def show_menu():

    print()
    print("====================================")
    print("     STUDENT PERFORMANCE ANALYZER")
    print("====================================")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Analyze Student")
    print("4. Show Top Student")
    print("5. Exit")


def view_students(students):

    print()
    print("========== ALL STUDENTS ==========")

    if len(students) == 0:
        print("No students added yet.")
        return

    for i, student in enumerate(students, start=1):

        print()
        print("Student", i)
        print("Name:", student["name"])
        print("Marks:", student["marks"])
        print("Attendance:", student["attendance"])

def save_students(students):

    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)

    print("Student data saved successfully! 💾")


def load_students():

    try:
        with open("students.json", "r") as file:
            students = json.load(file)

        return students

    except FileNotFoundError:
        return []


def analyze_student(students):

    print()
    print("========== ANALYZE STUDENT ==========")

    if len(students) == 0:
        print("No students added yet.")
        return

    for i, student in enumerate(students, start=1):
        print(f"{i}. {student['name']}")

    print()
    choice = input("Enter the student number: ")

    try:
        index = int(choice) - 1
        student = students[index]
    except (ValueError, IndexError):
        print("Invalid student number.")
        return

    score = calculate_performance(
        student["marks"],
        student["attendance"],
        student["assignment"],
        student["study_hours"],
        student["sleep_hours"]
    )

    print()
    print("Name:", student["name"])
    print("Study hours:", student["study_hours"])
    print("Attendance:", student["attendance"])
    print("Marks:", student["marks"])
    print("Assignment:", student["assignment"])
    print("Sleep hours:", student["sleep_hours"])
    print("Performance Score:", round(score, 2))
    print("Status:", get_status(score))

    give_suggestions(
        student["study_hours"],
        student["attendance"],
        student["marks"],
        student["assignment"],
        student["sleep_hours"]
    )


def show_top_student(students):

    print()
    print("========== TOP STUDENT ==========")

    if len(students) == 0:
        print("No students added yet.")
        return

    top_student = None
    top_score = -1

    for student in students:

        score = calculate_performance(
            student["marks"],
            student["attendance"],
            student["assignment"],
            student["study_hours"],
            student["sleep_hours"]
        )

        if score > top_score:
            top_score = score
            top_student = student

    print("Name:", top_student["name"])
    print("Performance Score:", round(top_score, 2))
    print("Status:", get_status(top_score))
    
    
# MAIN PROGRAM

students = load_students()

while True:

    show_menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student(students)
        save_students(students)
    

    elif choice == "2":
        view_students(students)
        
    elif choice == "3":
        analyze_student(students)

    elif choice == "4":
        show_top_student(students)

    elif choice == "5":
        print()
        print("Thank you for using Student Performance Analyzer!")
        break

    else:
        print()
        print("Invalid choice. Please try again.")