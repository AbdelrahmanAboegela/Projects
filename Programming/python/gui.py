from tkinter import *
import tkinter.messagebox

BG_COLOR = "#000000"
FG_COLOR = "#FFFFFF"
HL_COLOR = "#2ECC71"

class TodoList:
    def __init__(self):
        self.window = Tk()
        self.window.title("To-Do List")
        self.window.geometry("500x400")
        self.window.config(bg=BG_COLOR)

        self.task_frame = Frame(self.window, bg=BG_COLOR)
        self.task_frame.pack(padx=20, pady=20)

        self.task_label = Label(self.task_frame, text="To-Do List", font=("Helvetica", 18), bg=BG_COLOR, fg=FG_COLOR)
        self.task_label.pack(pady=10)

        self.task_listbox = Listbox(self.task_frame, bg="#101010", fg=FG_COLOR, height=10, width=50, font=("Helvetica", 12))
        self.task_listbox.pack(padx=10, pady=10, side=LEFT)

        self.task_scrollbar = Scrollbar(self.task_frame)
        self.task_scrollbar.pack(side=LEFT, fill=Y)

        self.task_listbox.config(yscrollcommand=self.task_scrollbar.set)
        self.task_scrollbar.config(command=self.task_listbox.yview)

        self.entry_frame = Frame(self.window, bg=BG_COLOR)
        self.entry_frame.pack(padx=20)

        self.entry_field = Entry(self.entry_frame, width=50, font=("Helvetica", 12), bg="#202020", fg=FG_COLOR)
        self.entry_field.pack(pady=10, side=LEFT)

        self.add_button = Button(self.entry_frame, text="Add", width=10, bg=HL_COLOR, fg="#FFFFFF", font=("Helvetica", 12), command=self.add_task)
        self.add_button.pack(pady=10, padx=(0, 10), side=LEFT)

        self.delete_button = Button(self.entry_frame, text="Delete", width=10, bg=HL_COLOR, fg="#FFFFFF", font=("Helvetica", 12), command=self.delete_task)
        self.delete_button.pack(pady=10, side=LEFT)

        self.mark_button = Button(self.entry_frame, text="Mark As Completed", width=20, bg=HL_COLOR, fg="#FFFFFF", font=("Helvetica", 12), command=self.mark_completed)
        self.mark_button.pack(pady=10, padx=(10, 0), side=LEFT)

        self.completed_frame = Frame(self.window, bg=BG_COLOR)
        self.completed_frame.pack(padx=20, pady=20)

        self.completed_label = Label(self.completed_frame, text="Completed Tasks", font=("Helvetica", 18), bg=BG_COLOR, fg=FG_COLOR)
        self.completed_label.pack(pady=10)

        self.completed_listbox = Listbox(self.completed_frame, bg="#202020", fg=FG_COLOR, height=3, width=50, font=("Helvetica", 12))
        self.completed_listbox.pack(padx=10, pady=10, side=LEFT)

        self.completed_scrollbar = Scrollbar(self.completed_frame)
        self.completed_scrollbar.pack(side=LEFT, fill=Y)

        self.completed_listbox.config(yscrollcommand=self.completed_scrollbar.set)
        self.completed_scrollbar.config(command=self.completed_listbox.yview)

        self.window.mainloop()

    def add_task(self):
        task_text = self.entry_field.get().strip()

        if not task_text:
            tkinter.messagebox.showerror("Error", "Please enter a task.")
            return

        self.task_listbox.insert(END, task_text)
        self.entry_field.delete(0, END)

    def delete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
        except IndexError:
            tkinter.messagebox.showerror("Error", "Please select a task to delete.")
            return

        task_text = self.task_listbox.get(index)
        self.task_listbox.delete(index)

        self.completed_listbox.insert(END, task_text)

    def mark_completed(self):
        try:
            index = self.task_listbox.curselection()[0]
        except IndexError:
            tkinter.messagebox.showerror("Error", "Please select a task to mark as completed.")
            return

        task_text = self.task_listbox.get(index)
        self.task_listbox.delete(index)

        self.completed_listbox.insert(END, task_text)

if __name__ == "__main__":
    todo_list = TodoList()