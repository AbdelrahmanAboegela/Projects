import tkinter as tk
from threading import Thread
import time

class DrawingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Multithreaded Drawing")

        self.canvas = tk.Canvas(self.master, width=300, height=200, bg="white")
        self.canvas.pack()

        # Start separate threads for drawing a circle and a rectangle
        circle_thread = Thread(target=self.draw_circle)
        rectangle_thread = Thread(target=self.draw_rectangle)

        circle_thread.start()
        rectangle_thread.start()

    def draw_circle(self):
        for i in range(200):
            self.canvas.delete("all")
            self.canvas.create_oval(i, 50, i + 50, 100, outline="blue")
            time.sleep(0.02)

    def draw_rectangle(self):
        for i in range(200):
            self.canvas.delete("all")
            self.canvas.create_rectangle(i, 150, i + 50, 180, outline="red")
            time.sleep(0.03)

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()
