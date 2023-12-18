class Employee:
    def _init_(self , ID , name , salary , dep):
        self.name = name
        self.ID = ID
        self.salary = salary
        self.dep = dep

    def assign_department (self , new_dep):
        self.dep=new_dep
        
    def print_employee_details(self):
        print(self.name)
        print(self.ID)
        print(self.salary)
        print(self.dep)
        
    def calculate_emp_salary(self , salary , hours):
        overtime=hours-50
        if(hours>50):
            return overtime*(salary/50)