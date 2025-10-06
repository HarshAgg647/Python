# Employee Management System

# Step 1 - Initialize Employee Data
employees = {
    101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000},
    102: {'name': 'Amit', 'age': 30, 'department': 'Finance', 'salary': 60000},
    103: {'name': 'Priya', 'age': 25, 'department': 'IT', 'salary': 55000}
}


# Step 3 - Add Employee Functionality
def add_employee():
    print("\n--- Add New Employee ---")
    emp_id = int(input("Enter Employee ID: "))
    if emp_id in employees:
        print("Employee ID already exists. Please enter a unique ID.")
        return

    name = input("Enter Employee Name: ").strip()
    age = int(input("Enter Employee Age: "))
    department = input("Enter Employee Department: ").strip()
    salary = float(input("Enter Employee Salary: "))

    employees[emp_id] = {
        'name': name,
        'age': age,
        'department': department,
        'salary': salary
    }
    print(f"Employee '{name}' added successfully!")

   


# Step 4 - View All Employees
def view_employees():
    print("\n--- All Employees ---")
    if not employees:
        print("No employees available.")
        return

    print("ID Name Age Department Salary")
    for emp_id, details in employees.items():
        print(emp_id, details['name'], details['age'], details['department'], details['salary'])
   

# Step 5 - Search Employee by ID
def search_employee():
    print("\n--- Search Employee ---")
    emp_id = int(input("Enter Employee ID to search: "))
    if emp_id in employees:
        emp = employees[emp_id]
        print(f"\nEmployee Found:")
        print(f"Name       : {emp['name']}")
        print(f"Age        : {emp['age']}")
        print(f"Department : {emp['department']}")
        print(f"Salary     : {emp['salary']}")
    else:
        print("Employee not found.")
   

# Step 2 & 6 - Main Menu System
def main_menu():
    while True:
        print("\n===== Employee Management System =====")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for Employee")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            print("\nThank you for using the Employee Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# Program Execution Entry Point
if __name__ == "__main__":
    main_menu()
