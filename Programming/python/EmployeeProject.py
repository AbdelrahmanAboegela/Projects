class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

class EmployeesManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print("Employee added successfully")

    def print_all_employees(self):
        for employee in self.employees:
            print(f"Employee: {employee.name} has age {employee.age} and salary {employee.salary}")

    def delete_employee_by_age(self, age):
        new_employees = []
        found_employee = False
        for employee in self.employees:
            if employee.age != age:
                new_employees.append(employee)
            else:
                found_employee = True
        if not found_employee:
            print("No employee found with that age.")
        else:
            self.employees = new_employees
            print("Employee(s) deleted successfully.")

    def update_salary_by_name(self, name, new_salary):
        found_employee = False
        for employee in self.employees:
            if employee.name == name:
                employee.salary = new_salary
                found_employee = True
                break
        if not found_employee:
            print("No employee found with that name.")
        else:
            print("Employee salary updated successfully.")


class FrontendManager:
    def __init__(self):
        self.employees_manager = EmployeesManager()

    def print_menu(self):
        print("Enter your choice:")
        print("1) Add new employee")
        print("2) Print all employees")
        print("3) Delete by age")
        print("4) Update salary by name")
        print("5) End the program")

    def get_choice(self):
        try:
            choice = int(input("Enter Your Choice:"))
            if choice < 1 or choice > 5:
                raise ValueError
            return choice
        except ValueError:
            print("Invalid choice. Please choose a number between 1 and 5.")
            return self.get_choice()

    def get_number_input(self, message):
        while True:
            try:
                number = float(input(message))
                return number
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def run(self):
        while True:
            self.print_menu()
            choice = self.get_choice()

            if choice == 1:
                name = input("Enter name: ")
                if not name.isalpha():
                    print("Invalid name. Please enter a valid string.")
                    continue
                age = self.get_number_input("Enter age: ")
                salary = self.get_number_input("Enter salary: ")
                employee = Employee(name, age, salary)
                self.employees_manager.add_employee(employee)

            elif choice == 2:
                self.employees_manager.print_all_employees()

            elif choice == 3:
                age = self.get_number_input("Enter age to delete: ")  
                self.employees_manager.delete_employee_by_age(age)

            elif choice == 4:
                name = input("Enter name to update: ")
                if not name.isalpha():
                    print("Invalid name. Please enter a valid string.")
                    continue
                new_salary = self.get_number_input("Enter new salary: ")
                self.employees_manager.update_salary_by_name(name, new_salary)

            elif choice == 5:
                break

        
if __name__ == '__main__':
    frontend_manager = FrontendManager()
    frontend_manager.run()
