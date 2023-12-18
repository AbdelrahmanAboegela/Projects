class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(f"({self.x}, {self.y})")
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def dist(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return ((dx ** 2) + (dy ** 2)) ** 0.5
#####################################################################
class Employee:
    def __init__(self, emp_id, emp_name, emp_salary, emp_department):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_department = emp_department
    
    def calculate_emp_salary(self, hours_worked):
        if hours_worked <= 50:
            return self.emp_salary
        else:
            overtime_hours = hours_worked - 50
            overtime_salary = (overtime_hours * (self.emp_salary / 50))
            return self.emp_salary + overtime_salary
    
    def assign_department(self, emp_department):
        self.emp_department = emp_department
    
    def print_employee_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Name: {self.emp_name}")
        print(f"Employee Salary: {self.emp_salary}")
        print(f"Employee Department: {self.emp_department}")
#######################################################################
class Inventory:
    def __init__(self):
        self.inventory_dict = {}
    
    def add_item(self, item_id, item_name, stock_count, price):
        item_dict = {"item_name": item_name, "stock_count": stock_count, "price": price}
        self.inventory_dict[item_id] = item_dict
    
    def update_item(self, item_id, item_name=None, stock_count=None, price=None):
        if item_id in self.inventory_dict:
            item_dict = self.inventory_dict[item_id]
            if item_name:
                item_dict["item_name"] = item_name
            if stock_count:
                item_dict["stock_count"] = stock_count
            if price:
                item_dict["price"] = price
        else:
            print("Item not found in inventory.")
    
    def check_item_details(self, item_id):
        if item_id in self.inventory_dict:
            item_dict = self.inventory_dict[item_id]
            print(f"Item ID: {item_id}")
            print(f"Item Name: {item_dict['item_name']}")
            print(f"Stock Count: {item_dict['stock_count']}")
            print(f"Price: {item_dict['price']}")
        else:
            print("Item not found in inventory.")
#######################################################################
class Rational:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    
    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Rational(new_numerator, new_denominator)
    
    def __sub__(self, other):
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Rational(new_numerator, new_denominator)
    
    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Rational(new_numerator, new_denominator)
    
    def __truediv__(self, other):
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Rational(new_numerator, new_denominator)
    
    def __eq__(self, other):
        return self.numerator * other.denominator == other.numerator * self.denominator
