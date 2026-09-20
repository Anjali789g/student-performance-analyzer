def add_student(students):

    print()
    print("========== ADD STUDENT ==========")

    name = input("Name: ")
    study_hours = float(input("Study hours per day: "))
    attendance = float(input("Attendance percentage: "))
    marks = float(input("Previous marks: "))
    assignment = float(input("Assignment score: "))
    sleep_hours = float(input("Sleep hours per day: "))

    student = {
        "name": name,
        "study_hours": study_hours,
        "attendance": attendance,
        "marks": marks,
        "assignment": assignment,
        "sleep_hours": sleep_hours
    }

    students.append(student)

    print()
    print("Student added successfully! ✅")


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

students = []

while True:

    show_menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student(students)

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