class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def printname(self):
        print(f"My name is {self.first_name} {self.last_name}")

class Student(Person):
    def __init__(self, first_name, last_name, grad_year):
        super().__init__(first_name, last_name)
        self.grad_year = grad_year

    def printname(self):
        print(f"My name is {self.first_name} {self.last_name}, and I'm graduating in {self.grad_year}")

class Gender(Person):
    def __init__(self, first_name, last_name, grad_year, gender):
        super().__init__(first_name, last_name)
        self.grad_year = grad_year
        self.gender = gender

    def print_gender(self):
        print(f"My gender is {self.gender}")
        
    def study(self):
        print(f"I am studying for my graduation in {self.grad_year}!")

gender = input("Enter your gender: ")
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
grad_year = input("Enter your graduation year: ")
student = Gender(first_name, last_name, grad_year, gender)
student.printname()
student.print_gender()
student.study()
####################################################
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def printname(self):
        print(f"My name is {self.first_name} {self.last_name}")

class Student(Person):
    def __init__(self, first_name, last_name, graduation_year):
        super().__init__(first_name, last_name)
        self.grad_year = graduation_year

    def printname(self):
        print(f"My name is {self.first_name} {self.last_name}, and I'm graduating in {self.grad_year}")

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
grad_year = input("Enter your graduation year: ")
student = Student(first_name, last_name, grad_year)
student.printname()
##############################################################
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def printname(self):
        print(f"My name is {self.first_name} {self.last_name}")

class Student(Person):
    def __init__(self, first_name, last_name, grad_year):
        super().__init__(first_name, last_name)
        self.grad_year = grad_year

    def printname(self):
        print(f"My name is {self.first_name} {self.last_name}, and I'm graduating in {self.grad_year}")

    def study(self):
        print(f"I am studying for my graduation in {self.grad_year}!")

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
grad_year = input("Enter your graduation year: ")
student = Student(first_name, last_name, grad_year)
student.printname()
student.study()