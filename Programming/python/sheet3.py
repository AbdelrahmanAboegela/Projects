import math
class Point:
    __slots__ = ['x', 'y']
    def __init__(self, x=0, y=0):
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
        return math.hypot(dx, dy)
if __name__ == "__main__":
    x1, y1 = input("Enter x1 and y1 separated by a space: ").split()
    p1 = Point(int(x1), int(y1))
    x2, y2 = input("Enter x2 and y2 separated by a space: ").split()
    p2 = Point(int(x2), int(y2))
    print("Initial positions:")
    p1.show()
    p2.show()
    dx, dy = input("Enter the amount to move p1 by in x and y directions separated by a space: ").split()
    p1.move(int(dx), int(dy))
    print("After moving p1:")
    p1.show()
    p2.show()
    print(f"Distance between p1 and p2: {p1.dist(p2)}")

#########################################################

class Employee:
    def __init__(self, emp_id, emp_name, emp_salary, emp_department):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_department = emp_department
    
    def calculate_emp_salary(self, hours_worked):
        if hours_worked <= 50:
            salary = self.emp_salary
        else:
            overtime = hours_worked - 50
            overtime_amount = (overtime * (self.emp_salary / 50))
            salary = self.emp_salary + overtime_amount
        return salary
    
    def emp_assign_department(self, new_department):
        self.emp_department = new_department
    
    def print_employee_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Name: {self.emp_name}")
        print(f"Employee Salary: {self.emp_salary}")
        print(f"Employee Department: {self.emp_department}")
        print()

if __name__ == "__main__":
    num_emp = int(input("Enter the number of employees: "))
    emp_list = []
    for i in range(num_emp):
        emp_id = input(f"Enter employee ID for employee {i+1}: ")
        emp_name = input(f"Enter employee name for employee {i+1}: ")
        emp_salary = float(input(f"Enter employee salary for employee {i+1}: "))
        emp_department = input(f"Enter employee department for employee {i+1}: ")
        emp = Employee(emp_id, emp_name, emp_salary, emp_department)
        new_department = input(f"Enter the new department for employee {i+1}: ")
        emp.emp_assign_department(new_department)
        emp_list.append(emp)

    hours_worked_list = []
    for i in range(num_emp):
        hours_worked = int(input(f"Enter the number of hours worked by employee {i+1}: "))
        hours_worked_list.append(hours_worked)

    for i in range(num_emp):
        salary = emp_list[i].calculate_emp_salary(hours_worked_list[i])
        emp_list[i].emp_salary = salary

    for emp in emp_list:
        emp.print_employee_details()
        
#############################################################        

class Inventory:
    def __init__(self):
        self.item_dict = {}

    def add_item(self, item_id, item_name, stock_count, price):
        self.item_dict[item_id] = {"item_name": item_name, "stock_count": stock_count, "price": price}

    def update_item(self, item_id, stock_count=None, price=None):
        item = self.item_dict.get(item_id)
        if item:
            if stock_count is not None:
                item["stock_count"] = stock_count
            if price is not None:
                item["price"] = price
        else:
            print(f"Item with ID {item_id} does not exist in inventory.")

    def check_item_details(self, item_id):
        item = self.item_dict.get(item_id)
        if item:
            return f"Item ID: {item_id}\nItem Name: {item['item_name']}\nStock Count: {item['stock_count']}\nPrice: {item['price']}"
        else:
            return f"Item with ID {item_id} does not exist in inventory."


if __name__ == "__main__":
    inventory = Inventory()

    while True:
        user_input = input("Are you an admin or a customer? Type 'A' for admin or 'C' for customer: ")

        if user_input == "A":
            while True:
                admin_input = input("Select an option:\n1. Add item\n2. Update item\n3. Check item details\n4. Exit\n")

                if admin_input == "1":
                    item_id = input("Enter item ID: ")
                    item_name = input("Enter item name: ")
                    stock_count = int(input("Enter stock count: "))
                    price = float(input("Enter price: "))

                    inventory.add_item(item_id, item_name, stock_count, price)
                    print("Item added successfully!")

                elif admin_input == "2":
                    item_id = input("Enter item ID: ")
                    stock_count = input("Enter stock count (leave blank to skip): ")
                    price = input("Enter price (leave blank to skip): ")

                    if stock_count or price:
                        if stock_count:
                            stock_count = int(stock_count)
                        else:
                            stock_count = None

                        if price:
                            price = float(price)
                        else:
                            price = None

                        inventory.update_item(item_id, stock_count, price)
                        print("Item updated successfully!")
                    else:
                        print("No changes were made.")

                elif admin_input == "3":
                    item_id = input("Enter item ID: ")
                    item_details = inventory.check_item_details(item_id)
                    print(item_details)

                elif admin_input == "4":
                    break

                else:
                    print("Invalid input. Please try again.")

        elif user_input == "C":
            item_id = input("Enter item ID: ")
            item_details = inventory.check_item_details(item_id)
            print(item_details)

        else:
            print("Invalid input. Please try again.")

#########################################################

class RationalNumber:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def simplify(self):
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)

        div = gcd(self.numerator, self.denominator)
        self.numerator //= div
        self.denominator //= div

    def add(self, other):
        new_num = self.numerator * other.denominator + other.numerator * self.denominator
        new_den = self.denominator * other.denominator
        result = RationalNumber(new_num, new_den)
        result.simplify()
        return result

    def subtract(self, other):
        new_num = self.numerator * other.denominator - other.numerator * self.denominator
        new_den = self.denominator * other.denominator
        result = RationalNumber(new_num, new_den)
        result.simplify()
        return result

    def multiply(self, other):
        new_num = self.numerator * other.numerator
        new_den = self.denominator * other.denominator
        result = RationalNumber(new_num, new_den)
        result.simplify()
        return result

    def divide(self, other):
        new_num = self.numerator * other.denominator
        new_den = self.denominator * other.numerator
        result = RationalNumber(new_num, new_den)
        result.simplify()
        return result

    def __eq__(self, other):
        return self.numerator * other.denominator == self.denominator * other.numerator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"


if __name__ == "__main__":
    while True:
        user_input = input("Select an option:\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Check Equality\n6. Exit\n")
        if user_input == "6":
            break
        try:
            num1 = int(input("Enter numerator for first fraction: "))
            den1 = int(input("Enter denominator for first fraction: "))
            num2 = int(input("Enter numerator for second fraction: "))
            den2 = int(input("Enter denominator for second fraction: "))
            frac1 = RationalNumber(num1, den1)
            frac2 = RationalNumber(num2, den2)
        except ValueError:
            print("Invalid input. Please enter integers only.")
            continue

        if user_input == "1":
            result = frac1.add(frac2)
            print(f"{frac1} + {frac2} = {result}")
        elif user_input == "2":
            result = frac1.subtract(frac2)
            print(f"{frac1} - {frac2} = {result}")
        elif user_input == "3":
            result = frac1.multiply(frac2)
            print(f"{frac1} * {frac2} = {result}")
        elif user_input == "4":
            if frac2.numerator == 0:
                print("Cannot divide by zero.")
                continue
            result = frac1.divide(frac2)
            print(f"{frac1} / {frac2} = {result}")
        elif user_input == "5":
            if frac1 == frac2:
                print(f"{frac1} and {frac2} are equal.")
            else:
                print(f"{frac1} and {frac2} are not equal.")
        else:
            print("Invalid input. Please try again.")
