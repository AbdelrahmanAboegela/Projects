import tkinter as tk
from tkinter import messagebox

ITEMS = {
    "Burger": 5.99,
    "Fries": 2.99,
    "Soft Drink": 1.99,
    "Ice Cream": 3.99,
    "Salad": 4.99
}

class BillManagementSystem:
    def __init__(self, master):
        self.master = master
        self.master.title("Bill Management System")
        self.master.geometry("400x400")

        self.label_title = tk.Label(self.master, text="Bill Management System", font=("Helvetica", 16))
        self.label_title.pack(pady=10)

        self.label_name = tk.Label(self.master, text="Name:")
        self.label_name.pack()

        self.entry_name = tk.Entry(self.master)
        self.entry_name.pack()

        self.label_item = tk.Label(self.master, text="Item:")
        self.label_item.pack()

        self.dropdown_item = tk.StringVar(self.master)
        self.dropdown_item.set(next(iter(ITEMS)))  # set default to first item
        self.optionmenu_item = tk.OptionMenu(self.master, self.dropdown_item, *ITEMS.keys())
        self.optionmenu_item.pack()

        self.label_quantity = tk.Label(self.master, text="Quantity:")
        self.label_quantity.pack()

        self.entry_quantity = tk.Entry(self.master)
        self.entry_quantity.pack()

        self.button_add = tk.Button(self.master, text="Add Bill", command=self.add_bill)
        self.button_add.pack(pady=10)

        self.listbox_bills = tk.Listbox(self.master)
        self.listbox_bills.pack()

        self.button_remove = tk.Button(self.master, text="Remove Selected Bill", command=self.remove_bill)
        self.button_remove.pack(pady=10)

        self.label_total = tk.Label(self.master, text="Total: $0.00", font=("Helvetica", 14))
        self.label_total.pack(pady=10)

    def add_bill(self):
        name = self.entry_name.get()
        item = self.dropdown_item.get()
        quantity = self.entry_quantity.get()

        if not name or not item or not quantity:
            messagebox.showwarning("Warning", "Please enter name, item, and quantity.")
            return

        try:
            quantity = int(quantity)
        except ValueError:
            messagebox.showwarning("Warning", "Quantity must be a whole number.")
            return

        price = ITEMS[item]
        total = price * quantity

        bill_str = f"{name} - {item} x {quantity} - ${total:.2f}"
        self.listbox_bills.insert(tk.END, bill_str)

        self.entry_name.delete(0, tk.END)
        self.entry_quantity.delete(0, tk.END)

        self.update_total()

    def remove_bill(self):
        selected = self.listbox_bills.curselection()

        if not selected:
            messagebox.showwarning("Warning", "Please select a bill to remove.")
            return

        self.listbox_bills.delete(selected)

        self.update_total()

    def update_total(self):
        total = 0.0
        for i in range(self.listbox_bills.size()):
            bill_str = self.listbox_bills.get(i)
            total += float(bill_str.split("$")[-1].strip())

        self.label_total.config(text=f"Total: ${total:.2f}")

root = tk.Tk()
app = BillManagementSystem(root)
root.mainloop()