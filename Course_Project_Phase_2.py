# Joshua Flye, CIS261, Course Project Phase 2: Using Lists and Dictionaries to Store and Retrieve Data

import datetime

def get_date_input(prompt):
    while True:
        date_str = input(prompt)
        try:
            date_obj = datetime.datetime.strptime(date_str,"%m/%d/%Y").date()
            return date_obj
        except ValueError:
            print("Invalid date format. Please use mm/dd/yyyy.")

def get_float_input(prompt):
    while True:
        try:
            value_str = input(prompt)
            value = float(value_str)
            if value < 0:
                print("Value cannot be negative. Please try again.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_positive_float_input(prompt):
    while True:
        value = get_float_input(prompt)
        if value > 0:
            return value
        else:
            print("Value must be greater than zero. Please try again.")

def get_positive_integer_input(prompt):
    while True:
        try:
            value_str = input(prompt)
            value = int(value_str)
            if value > 0:
                return value
            else:
                print("Invalid input. Please enter an integer.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

 def get_employee_data_from_user():
     print("\nEnter Employee Details:")
                

