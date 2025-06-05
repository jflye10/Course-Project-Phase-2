# Joshua Flye, CIS261, Course Project Phase 2: Using Lists and Dictionaries to Store and Retrieve Data

import datetime

def get_dates_for_hours_worked():
    """
    Inputs and returns the 'from' date and 'to' date for hours worked.
    Dates must be in format mm/dd/yyyy.
    """
    while True:
        from_date_str = input("Enter the 'from' date (mm/dd/yyyy): ")
        to_date_str = input("Enter the 'to' date (mm/dd/yyyy): ")
        try:
            from_date = datetime.datetime.strptime(from_date_str, "%m/%d/%Y").strftime("%m/%d/%Y")
            to_date = datetime.datetime.strptime(to_date_str, "%m/%d/%Y").strftime("%m/%d/%Y")
            return from_date, to_date
        except ValueError:
            print("Invalid date format. Please use mm/dd/yyyy.")

def calculate_employee_pay(employee_data_list):
    """
    Reads through the list(s) of employee data, calculates income tax and net pay.
    and displays the details for each employee.
    Increments and stores totals in a dictionary object.
    """

    overall_totals = {
        "total_employees": 0,
        "total_hours": 0.0,
        "total_tax": 0.0,
        "total_net_pay": 0.0
    }

    print("\n--- Employee Pay Details ---")
    for employee in employee_data_list:
        from_date = employee["from_date"]
        to_date = employee["to_date"]
        employee_name = employee["employee_name"]
        total_hours = employee["total_hours"]
        hourly_rate = employee["hourly_rate"]
        income_tax_rate = employee["income_tax_rate"]

        gross_pay = total_hours * hourly_rate
        income_taxes = gross_pay * income_tax_rate
        net_pay = gross_pay - income_taxes

        print(f"\nEmployee Name: {employee_name}")
        print(f"From Date: {from_date}")
        print(f"To Date: {to_date}")
        print(f"Hours Worked: {total_hours:.2f}")
        print(f"Hourly Rate: ${hourly_rate:.2f}")
        print(f"Gross Pay: ${gross_pay:.2f}")
        print(f"Income Tax Rate: {income_tax_rate:.2f%}")
        print(f"Income Taxes: ${income_taxes:.2f}")
        print(f"Net Pay: ${net_pay:.2f}")
        
        overall_totals["total_employees"] += 1
        overall_totals["total_hours"] += total_hours
        overall_totals["total_tax"] += income_taxes
        overall_totals["total_net_pay"] += net_pay

    def display_overall_totals(totals_data):
        """
        Displays the overall totals(totals_data):
        Reads data from the provided dictionary object.
        """
        print("\n--- Overall Totals ---")
        print(f"Total Number of Employees: {totals_data['total_employees']}")
        print(f"Total Hours Worked: {totals_data['total_hours']:.2f}")
        print(f"Total Income Tax Paid: ${totals_data['total_tax']:.2f}")
        print(f"Total Net Pay Distributed: ${totals_data['total_net_pay']:.2f}")
    
    def main():
        """
        Main fucntion to run the employee payroll system.
        """
        all_employees_data = []

        while True:
            from_date, to_date = get_dates_for_hours_worked()

            employee_name = input("Enter employee name (or 'done' to finish): ")
            if employee_name.lower() == 'done':
                break

            while True:
                try:
                    total_hours = float(input("Enter total hours worked: "))
                    if total_hours < 0:
                        print("Hours worked cannot be negative. Please enter a valid number.")
                    else:
                        break
                except ValueError:
                    print("Invalid input. Please enter a number for hours worked.")

            while True:
                try:
                    income_tax_rate = float(input("Enter income tax rate (e.g., 0.15 for 15%): "))
                    if not (0 <= income_tax_rate <= 1):
                        print("Incomme tax rate must be between 0 and 1. Please enter a valid number.")
                    else:
                        break
                except ValueError:
                    print("Invalid input. Pkease enter a number for income tax rate.")
            employee_info = {
                "from_date": from_date,
                "to_date": to_date,
                "employee_name": employee_name,
                "total_hours": total_hours,
                "hourly_rate": hourly_rate,
                "income_tax_rate": income_tax_rate

            }
            all_employees_data.append(employee_info)

        if not all_employees_data:
            print("No employee data entered.")
            return

        overall_totals_data = calculate_employee_pay(all_employees_data)
        display_overall_totals(overall_totals_data)

    if __name__ == "__main__":
        main()