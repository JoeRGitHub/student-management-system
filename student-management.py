
import re
import tabulate
import statistics

students = []


# ------------------------------ Main menu ------------------------------- #
def show_menu():
    print("""
    Welcome to the Student Management System!
    1. Add a Student.
    2. View All Students.
    3. Calculate Average Score.
    4. Find the Highest Scorer.
    5. Exit.
    """)

    while True:
        user_choice = input("choice? ")
        if user_choice != "5":
            pass
        else:
            print("Student Management System Closed")
            break


# ------------------------------ Validatetion  ------------------------------- #
def validate_name_field(prompt):
    while True:
        name = input(prompt)
        if re.fullmatch('[a-zA-Z ]+', name):
            return name
        else:
            print("enter a valid name without nummbers")


def validate_score(prompt):
    while True:
        try:
            score = int(input(prompt))
            if 0 <= score <= 100:
                return score
            else:
                print("Score must be between 0 and 100")
        except ValueError:
            print("Enter a valid integer score: ")

# ------------------------------ Adding students ------------------------------- #


def add_student():
    while True:
        student_name = validate_name_field("Add student full name: ")
        student_field = validate_name_field("Add student field: ")
        student_score = validate_score("Add student score: ")

        students.append(
            {
                "name": student_name,
                "field": student_field,
                "score": student_score
            }
        )
        print(students)

        another = input("Add another student (y/n)? \n")
        if another != "y":
            break

# ------------------------------ Calculatetion ------------------------------- #


def calculate_average(ave_score):
    list = []
    for i in ave_score:
        list.append(i["score"])
    print("\nCalculate average score all students: ", statistics.mean(list))


def highest_scorer(highest_score):
    score = 0
    for i in highest_score:
        if i["score"] > score:
            i["score"] == score
    print("\nHighest Scorer:", i["name"], i["score"])

# ------------------------------ Table view ------------------------------- #


def view_students():
    # header = list(students[0].keys())
    # for i in header:
    #     y = i.capitalize()
    header = list(students[0].keys())
    rows = []
    for i in students:
        rows.append(i.values())
        # rows = [x.values() for x in students]
    print(tabulate.tabulate(rows, header))

# ------------------------------ Main function ------------------------------- #


def main():
    show_menu()


view_students()
add_student()
view_students()
calculate_average(students)
highest_scorer(students)
