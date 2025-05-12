# Joshua Flye, CIS261, Course Project Phase 2

from traceback import print_exception
from datetime import datetime

def get_date_range():
    """
    Gets the from and to dates for the work period from the user.
    """
    while True:
        from_date_str = input("Enter the from date (mm/dd/yyyy): ")
        to_date_str = input("Enter the to date (mm/dd/yyyy): ")
        try:
            from_date = datetime.strptime(from_date_str, "%m/%d/%Y").date()
            to_date = datetime.strptime(to_date_str, "%m/%d,%Y").date()
            if from_date <= to_date:
                return from_date, to_date
            else:
                print("Error: The 'from date' must be before or the same as the 'to date'.")
        except ValueError:
            print("Invalid date format. Please use mm/dd/yyyy.")

def get_employee_name():
    """
    Gets the employee's name from the user.
    """
    while True:
        name = input("Enter employee name (or 'end' to finish): ").strip()
        if name:
            return name
        print("Employee name cannot be empty. Please enter a valid name.")

def get_total_hours():
    """
    Gets the total hours worked from the user.
    """
    while True:
        try:
            hours = float(input("Enter total hours: "))
            if hours >= 0:
                return hours
            else:
                print("Hours must be a non-negative number.")
        except ValueError:
            print("Invalid input. Please enter a numeric value for hours.")

def get_hourly_rate():
    """
    Gets the hourly rate from the user.
    """
    while True:
        try:
            rate = float(input("Enter hourly rate: "))
            if rate >= 0:
                return rate
            else:
                print("Hourly rate must be a non-negative number.")
        except ValueError:
            print("Invalid input. Please enter a numeric value for the tax rate.")
def get_income_tax():
    """
    Gets the income tax rate from the user (as a decimal between 0 and 1).
    """
    while True:
        try:
            tax_rate = float(input("Enter income tax rate (e.g., 0.15 for 15%): "))
            if 0 <= tax_rate <= 1:
                return tax_rate
            else:
                print("Tax rate must be between 0 and 1.")
        except ValueError:
            print("Invalid input. Please enter a numeric vallue for the tax rate.")

def calculate_pay(hours, rate, tax_rate):
    """
    Calculates gross pay, income tax, and net pay.
    """
    gross_pay = hours * rate
    income_tax = gross_pay * tax_rate
    net_pay = gross_pay - income_tax
    return gross_pay, income_tax, net_pay

def display_employee_info(employee_data):
    """
    Displays the employee's information.
    """
    from_date, to_date, name, hours, rate, gross_pay, tax_rate, income_tax, net_pay = employee_data
    print("\n--- Employee Information ---")
    print(f"From Date: {from_date.strftime('%m/%d/%Y')}")
    print(f"To Date:{to_date.strftime('%m/%d/%Y')}")
    print(f"Name: {name}")
    print(f"Total Hours: {hours:.2f}")
    print(f"Hourly Rate: ${rate:.2f}")
    print(f"Gross Pay: ${gross_pay:.2f}")
    print(f"Income Tax Rate: {tax_rate:.2%}")
    print(f"Income Taxes: ${income_tax:.2f}")
    print(f"Net Pay: ${net_pay:.2f}")

def display_totals(totals):
    """
    Displays the overall totals.
    """
    print("\n--- Overall Totals ---")
    print(f"Total Employees: {totals['num_employees']}")
    print(f"Total Hours Worked: {totals['total_hours']:.2f}")
    print(f"Total Income Tax: {totals['total_tax']:.2f}")
    print(f"Total Net Pay: ${totals['total_net_pay']:.2f}")

def main():
    """
    Main function to run the program.
    """
    employee_data_list = []
    totals = {
        'num_employees': 0,
        'total_hours': 0.0,
        'total_gross_pay': 0.0,
        'total_tax': 0.0,
        'total_net_pay': 0.0,
    }

    while True:
        from_date, to_date = get_date_range()
        name = get_employee_name()
        if name.lower() == 'end':
            break

        hours = get_total_hours()
        rate = get_hourly_rate()
        tax_rate = get_income_tax_rate()

        gross_pay, income_tax, net_pay = calculate_pay(hours, rate, tax_rate)

        employee_data = [from_date, to_date, name, hours, rate, gross_pay,tax_rate, income_tax, net_pay]
        employee_data_list.append(employee_data)

    if employee_data_list:
        for data in employee_data_list:
            display_employee_info(data)
            totals['num_employees'] += 1
            totals['total_hours'] += data[3]
            totals['total)gross_pay'] += data[5]
            totals['total_tax'] += data[7]
            totals['total_net_pay'] += data[8]

        display_totals(totals)
    else:
        print("No employee data entered.")
        print("Exiting program.")

if __name__ == "__main__":
    main()

