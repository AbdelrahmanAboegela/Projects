class Employee:
    def __init__(self, emp_id, emp_name, emp_salary, emp_department, emp_age):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_department = emp_department
        self.emp_age = emp_age

    def calculate_emp_salary(self, hours_worked, overtime_cost):
        if hours_worked <= 50:
            salary = self.emp_salary
        else:
            overtime = hours_worked - 50
            overtime_amount = (overtime * overtime_cost)
            salary = self.emp_salary + overtime_amount
        return salary

    def update_employee_details(self, emp_name, emp_salary, emp_department):
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_department = emp_department

    def print_employee_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Name: {self.emp_name}")
        print(f"Employee Salary: {self.emp_salary}")
        print(f"Employee Department: {self.emp_department}")
        print(f"Employee Age: {self.emp_age}")
        print()

def read_employee_data():
    try:
        with open("C:/Users/Blu-Ray/Desktop/EMP.txt", "r") as f:
            emp_list = []
            for line in f:
                emp_data = line.strip().split(",")
                emp = Employee(emp_data[0], emp_data[1], float(emp_data[2]), emp_data[3], int(emp_data[4]))
                emp_list.append(emp)
            return emp_list
    except FileNotFoundError:
        return []

def write_employee_data(emp_list):
    with open("C:/Users/Blu-Ray/Desktop/EMP.txt", "w") as f:
        for emp in emp_list:
            emp_data = [emp.emp_id, emp.emp_name, str(emp.emp_salary), emp.emp_department, str(emp.emp_age)]
            f.write(",".join(emp_data) + "\n")

def print_all_employees(emp_list):
    result = ""
    for emp in emp_list:
        result += f"Employee ID: {emp.emp_id}\n"
        result += f"Employee Name: {emp.emp_name}\n"
        result += f"Employee Salary: {emp.emp_salary}\n"
        result += f"Employee Department: {emp.emp_department}\n"
        result += f"Employee Age: {emp.emp_age}\n\n"
    return result

def print_employee_by_id(emp_list, emp_id):
    for emp in emp_list:
        if emp.emp_id == emp_id:
            emp.print_employee_details()
            return
    print("Employee not found.")

def add_employee(emp_list):
    emp_id = input("Enter employee ID: ")
    emp_name = input("Enter employee name: ")
    emp_salary = float(input("Enter employee salary: "))
    emp_department = input("Enter employee department: ")
    emp_age = int(input("Enter employee age: "))
    emp = Employee(emp_id, emp_name, emp_salary, emp_department, emp_age)
    emp_list.append(emp)
    write_employee_data(emp_list)
    print("Employee added successfully!")
    return emp_list

def delete_employee(emp_list):
    print("Select the field to delete by:")
    print("1. ID")
    print("2. Name")
    print("3. Age")
    choice = int(input("Enter your choice: "))
    deleted = False
    if choice == 1:
        emp_id = input("Enter the ID of the employee to delete: ")
        for emp in emp_list[:]:
            if emp.emp_id == emp_id:
                emp_list.remove(emp)
                deleted = True
    elif choice == 2:
        emp_name = input("Enter the name of the employee to delete: ")
        for emp in emp_list[:]:
            if emp.emp_name == emp_name:
                emp_list.remove(emp)
                deleted = True
    elif choice == 3:
        emp_age = int(input("Enter the age of the employees to delete: "))
        for emp in emp_list[:]:
            if emp.emp_age == emp_age:
                emp_list.remove(emp)
                deleted = True
    if deleted:
        write_employee_data(emp_list)
        print("Employee(s) deleted successfully!")
    else:
        print("No employees found.")
    return emp_list

def assign_work_hours(emp_list, overtime_cost):
    emp_id = input("Enter employee ID to assign work hours: ")
    hours_worked = int(input("Enter the number of hours worked by the employee: "))
    for emp in emp_list:
        if emp.emp_id == emp_id:
            salary = emp.calculate_emp_salary(hours_worked, overtime_cost)
            emp.emp_salary = salary
            emp.print_employee_details()
            write_employee_data(emp_list)
            break
    else:
        print("Employee not found.")
    return emp_list

def update_employee_info(emp_list):
    emp_id = input("Enter employee ID to update info: ")
    for i, emp in enumerate(emp_list):
        if emp.emp_id == emp_id:
            print("Select the fields to update:")
            print("1. Name")
            print("2. Age")
            print("3. Salary")
            print("4. Department")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                emp_name = input("Enter employee name: ")
                emp.emp_name = emp_name
            elif choice == 2:
                emp_age = int(input("Enter employee age: "))
                emp.emp_age = emp_age
            elif choice == 3:
                emp_salary = float(input("Enter employee salary: "))
                emp.emp_salary = emp_salary
            elif choice == 4:
                emp_department = input("Enter employee department: ")
                emp.emp_department = emp_department
            emp_list[i] = emp
            emp.print_employee_details()
            write_employee_data(emp_list)
            break
    else:
        print("Employee not found.")
    return emp_list

if __name__ == "__main__":
    emp_list = read_employee_data()
    while True:
        user_type = input("Are you an admin or a customer? Type 'A' for admin or 'EMP' for employee: ")
        if user_type == "A":
            overtime_cost = 0
            while True:
                # Admin options
                print("Options:")
                print("1. Add employee")
                print("2. Assign work hours")
                print("3. Set overtime cost per hour")
                print("4. Update employee info")
                print("5. Print all employees")
                print("6. Print employee by ID")
                print("7. Delete employee by:")
                print("8. Exit")
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    emp_list = add_employee(emp_list)
                elif choice == 2:
                    emp_list = assign_work_hours(emp_list, overtime_cost)
                elif choice == 3:
                    overtime_cost = float(input("Enter the cost per hour for overtime: "))
                elif choice == 4:
                    emp_list = update_employee_info(emp_list)
                elif choice == 5:
                    print(print_all_employees(emp_list))
                elif choice == 6:
                    emp_id = input("Enter employee ID: ")
                    print_employee_by_id(emp_list, emp_id)
                elif choice == 7:
                    emp_list = delete_employee(emp_list)
                elif choice == 8:
                    break
                else:
                    print("Invalid choice, please try again.")
        elif user_type == "EMP":
            # Employee options
            print("Options:")
            print("1. View my details")
            print("2. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                emp_id = input("Enter your employee ID: ")
                print_employee_by_id(emp_list, emp_id)
            elif choice == 2:
                break
            else:
                print("Invalid choice, please try again.")
        else:
            print("Invalid user type, please try again.")

    write_employee_data(emp_list)
    print("Program terminated.")
