
import re
import tabulate
import statistics

students = []

# ------------------------------ Main menu ------------------------------- #


def menu():

    while True:
        print("""
        Welcome to the Student Management System!
        1. Add a student.
        2. View all students.
        3. Calculate average score.
        4. Find the highest scorer.
        5. Exit.
        """)
        user_choice = input("Choice form the meny? ")
        if user_choice == "1":
            add_student()
        elif user_choice == "2":
            view_students()
        elif user_choice == "3":
            calculate_average(students)
        elif user_choice == "4":
            highest_scorer(students)
        elif user_choice == "5":
            print("\nStudent Management System closed")
            break
        elif user_choice == "6":
            search()
        else:
            print("\nUnrecognized character. Try again.")


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
    update_name = 0
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

        print(
            f"Student {students[update_name]['name']} was added successfully!")
        update_name += 1
        another = input("Add another student (y/n)? \n")
        if another != "y":
            break

# ------------------------------ Calculatetion ------------------------------- #


def calculate_average(ave_score):
    try:
        list = []
        for i in ave_score:
            list.append(i["score"])
        print("\nCalculate average score all students: ",
              round(statistics.mean(list), 2))
    except statistics.StatisticsError:
        print("\nNo students available.")


def highest_scorer(highest_score):
    try:
        score = 0
        for i in highest_score:
            if i["score"] > score:
                i["score"] == score
        print("\nHighest Scorer:", i["name"], i["score"])
    except UnboundLocalError:
        print("\nNo students available.")

# ------------------------------ Table view ------------------------------- #


def view_students():
    try:
        header = list(students[0].keys())
        rows = []
        for i in students:
            rows.append(i.values())
            # rows = [x.values() for x in students]
        print(f"\n{tabulate.tabulate(rows, header)}")
    except IndexError:
        print("\nNo students available.")

# ------------------------------ Search | Delete ----------------------------- #


def search():
    # print(students)

    search_student = input("Enter a student name to search: ").lower()
    found = False
    for student in students:
        # print(f'search_student: {search_student}')
        # print(student.get("name"))

        # Used in to find part of string in string
        if search_student in student.get("name").lower():
            print(
                f'\nStudent info {student.get("name")} - \nField: {student.get("field")}\nScore: {student.get("score")}')
            found = True

    if not found:
        print("\nNo students available.")

# ------------------------------ Main function ------------------------------- #


if __name__ == "__main__":
    menu()
