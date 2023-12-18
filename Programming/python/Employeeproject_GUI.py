import tkinter as tk
from tkinter import messagebox

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

    def delete_employee_by_age(self, age):
        self.employees = [employee for employee in self.employees if employee.age != age]

    def update_salary_by_name(self, name, new_salary):
        for employee in self.employees:
            if employee.name == name:
                employee.salary = new_salary

class FrontendManagerGUI:
    def __init__(self):
        self.employees_manager = EmployeesManager()
        
        self.root = tk.Tk()
        self.root.title("Employee Manager")
        self.root.geometry("300x400")
        
        self.name_label = tk.Label(self.root, text="Name:")
        self.name_entry = tk.Entry(self.root)
        self.age_label = tk.Label(self.root, text="Age:")
        self.age_entry = tk.Entry(self.root)
        self.salary_label = tk.Label(self.root, text="Salary:")
        self.salary_entry = tk.Entry(self.root)
        self.add_button = tk.Button(self.root, text="Add Employee", command=self.add_employee)
        self.print_button = tk.Button(self.root, text="Print Employees", command=self.print_employees)
        self.delete_label = tk.Label(self.root, text="Delete Employee by Age:")
        self.delete_entry = tk.Entry(self.root)
        self.delete_button = tk.Button(self.root, text="Delete Employee", command=self.delete_employee)
        self.update_label = tk.Label(self.root, text="Update Employee Salary by Name:")
        self.update_name_entry = tk.Entry(self.root)
        self.update_salary_label = tk.Label(self.root, text="New Salary:")
        self.update_salary_entry = tk.Entry(self.root)
        self.update_button = tk.Button(self.root, text="Update Salary", command=self.update_salary)
        


        self.name_label.pack()
        self.name_entry.pack()
        self.age_label.pack()
        self.age_entry.pack()
        self.salary_label.pack()
        self.salary_entry.pack()
        self.add_button.pack()
        self.print_button.pack()
        self.delete_label.pack()
        self.delete_entry.pack()
        self.delete_button.pack()
        self.update_label.pack()
        self.update_name_entry.pack()
        self.update_salary_label.pack()
        self.update_salary_entry.pack()
        self.update_button.pack()
    
    def add_employee(self):
        name = self.name_entry.get()
        age = int(self.age_entry.get())
        salary = int(self.salary_entry.get())
        employee = Employee(name, age, salary)
        self.employees_manager.add_employee(employee)
        messagebox.showinfo("Success", "Employee added successfully.")
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.salary_entry.delete(0, tk.END)
        
    def print_employees(self):
        if not self.employees_manager.employees:
            messagebox.showinfo("Error", "No employees to print.")
        else:
            message = "Employees:\n"
            for employee in self.employees_manager.employees:
                message += f" {employee.name} has age {employee.age} and salary {employee.salary}\n"
            messagebox.showinfo("Employees", message)
            
    def delete_employee(self):
        try:
            age = int(self.delete_entry.get())
            self.employees_manager.delete_employee_by_age(age)
            messagebox.showinfo("Success", "Employee deleted successfully.")
            self.delete_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Invalid age.")

    def update_salary(self):
        name = self.update_name_entry.get()
        new_salary = self.update_salary_entry.get()
        try:
            new_salary = int(new_salary)
            self.employees_manager.update_salary_by_name(name, new_salary)
            messagebox.showinfo("Success", "Salary updated successfully.")
            self.update_name_entry.delete(0, tk.END)
            self.update_salary_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Invalid salary.")
        
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = FrontendManagerGUI()
    app.run()