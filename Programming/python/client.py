import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, simpledialog

def create_new_user_window():
    username = simpledialog.askstring("Username", "Enter your username:")
    if username:
        client = ChatClient(username)
        client.root.mainloop()

class ChatClient:
    def __init__(self, username):
        self.username = username
        self.root = tk.Tk()
        self.root.title(f"Chat Room - {self.username}")

        self.messages_text_area = scrolledtext.ScrolledText(self.root)
        self.messages_text_area.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

        self.entry_text_area = scrolledtext.ScrolledText(self.root)
        self.entry_text_area.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

        send_button = tk.Button(self.root, text="Send", command=self.send)
        send_button.pack(padx=10, pady=10)

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(("localhost", 9999))

        receive_thread = threading.Thread(target=self.receive)
        receive_thread.daemon = True
        receive_thread.start()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def receive(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode()
                self.messages_text_area.insert(tk.END, message + "\n")
            except:
                print("An error occurred while receiving messages.")
                break

    def send(self):
        message = self.entry_text_area.get("1.0", tk.END).strip()
        if message:
            try:
                self.client_socket.send(f"{self.username}: {message}".encode())
            except:
                print("An error occurred while sending the message.")
            self.entry_text_area.delete("1.0", tk.END)

    def on_closing(self):
        self.client_socket.send("/quit".encode())
        self.client_socket.close()
        self.root.destroy()

root = tk.Tk()
root.title("Main Window")

create_button = tk.Button(root, text="Create New User Window", command=create_new_user_window)
create_button.pack(padx=10, pady=10)

root.mainloop()
