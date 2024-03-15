import tkinter as tk
from tkinter import ttk
import cx_Oracle

class PharmacyManagementSystem:
    def _init_(self, root):
        self.root = root
        self.root.title("Pharmacy Management System")
        self.root.geometry("800x600")

        self.connection = cx_Oracle.connect("your_username", "your_password", "your_oracle_connection_string")
        self.cursor = self.connection.cursor()

        self.create_tabs()
        self.create_medications_tab()
        self.create_customers_tab()

    def create_tabs(self):
        self.tabControl = ttk.Notebook(self.root)
        self.tabControl.pack(expand=1, fill="both")

        self.medicationsTab = ttk.Frame(self.tabControl)
        self.tabControl.add(self.medicationsTab, text="Medications")

        self.customersTab = ttk.Frame(self.tabControl)
        self.tabControl.add(self.customersTab, text="Customers")

    def create_medications_tab(self):
        self.medications_tree = ttk.Treeview(self.medicationsTab, columns=("MedicationID", "Name", "UnitPrice", "ExpiryDate"))
        self.medications_tree.heading("#0", text="Index")
        self.medications_tree.heading("MedicationID", text="Medication ID")
        self.medications_tree.heading("Name", text="Name")
        self.medications_tree.heading("UnitPrice", text="Unit Price")
        self.medications_tree.heading("ExpiryDate", text="Expiry Date")

        self.medications_tree.column("#0", stretch=tk.NO)
        self.medications_tree.column("MedicationID", anchor=tk.CENTER, width=100)
        self.medications_tree.column("Name", anchor=tk.W, width=200)
        self.medications_tree.column("UnitPrice", anchor=tk.CENTER, width=100)
        self.medications_tree.column("ExpiryDate", anchor=tk.CENTER, width=150)

        self.medications_tree.pack(expand=1, fill="both")

        self.load_medications_data()

    def create_customers_tab(self):
        self.customers_tree = ttk.Treeview(self.customersTab, columns=("CustomerID", "FirstName", "LastName", "DateOfBirth", "Phone", "Email"))
        self.customers_tree.heading("#0", text="Index")
        self.customers_tree.heading("CustomerID", text="Customer ID")
        self.customers_tree.heading("FirstName", text="First Name")
        self.customers_tree.heading("LastName", text="Last Name")
        self.customers_tree.heading("DateOfBirth", text="Date of Birth")
        self.customers_tree.heading("Phone", text="Phone")
        self.customers_tree.heading("Email", text="Email")

        self.customers_tree.column("#0", stretch=tk.NO)
        self.customers_tree.column("CustomerID", anchor=tk.CENTER, width=100)
        self.customers_tree.column("FirstName", anchor=tk.W, width=150)
        self.customers_tree.column("LastName", anchor=tk.W, width=150)
        self.customers_tree.column("DateOfBirth", anchor=tk.CENTER, width=100)
        self.customers_tree.column("Phone", anchor=tk.CENTER, width=100)
        self.customers_tree.column("Email", anchor=tk.W, width=200)

        self.customers_tree.pack(expand=1, fill="both")

        self.load_customers_data()

    def load_medications_data(self):
        query = "SELECT * FROM Medications"
        self.cursor.execute(query)
        medications_data = self.cursor.fetchall()

        for index, medication in enumerate(medications_data):
            self.medications_tree.insert("", index, values=medication)

    def load_customers_data(self):
        query = "SELECT * FROM Customers"
        self.cursor.execute(query)
        customers_data = self.cursor.fetchall()

        for index, customer in enumerate(customers_data):
            self.customers_tree.insert("", index, values=customer)

if _name_ == "_main_":
    root = tk.Tk()
    app = PharmacyManagementSystem(root)
    root.mainloop()