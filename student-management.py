
import re
import os

students = []


# ------------------------------ Main Menu ------------------------------- #
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


# ------------------------------ Adding students ------------------------------- #
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

        another = input("Add another student (y/n)? ")
        print(another)
        if another != "y":
            break

# ------------------------------ Main function ------------------------------- #


def main():
    show_menu()


# main()
add_student()

# students.update({student_name: student_score})

# def update_cart(item_to_cart, quantity_to_cart):
#     cart_items.update({item_to_cart: quantity_to_cart})
#     product_prices.update({item_to_cart: create_price()})
#     print(product_prices)
#     print(cart_items)

# # ------------------------- Calculation ------------------------------- #


# def calculate_cart_total(cart_items, product_prices):
#     """
#     Calculates the total price of all items in the cart.

#     """
#     total = 0
#     for product, quantity in cart_items.items():
#         total += quantity * product_prices.get(product, 0)
#     return round(total, 2)
