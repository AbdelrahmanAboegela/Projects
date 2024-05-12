import tkinter as tk
from tkinter import ttk
import socket

def send_request():
    operation = operation_var.get()
    message = message_entry.get()
    key = int(key_entry.get())

    if operation not in ['encrypt', 'decrypt']:
        result_var.set("Invalid operation.")
        return

    host = '127.0.0.1'
    port = 5555

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        try:
            client_socket.connect((host, port))
            request = f"{operation},{message},{key}"
            client_socket.send(request.encode())
            response = client_socket.recv(1024).decode()
            result_var.set(response)
        except ConnectionRefusedError:
            result_var.set("Connection refused. Server is not running.")

# Create main window
root = tk.Tk()
root.title("Message Encryptor/Decryptor")

# Frame for message input and operation selection
input_frame = ttk.Frame(root, padding="20")
input_frame.pack()

ttk.Label(input_frame, text="Message:").grid(row=0, column=0, sticky="w")
message_entry = ttk.Entry(input_frame, width=40)
message_entry.grid(row=0, column=1, padx=10)

ttk.Label(input_frame, text="Key (integer):").grid(row=1, column=0, sticky="w")
key_entry = ttk.Entry(input_frame, width=10)
key_entry.grid(row=1, column=1, padx=10)

operation_var = tk.StringVar()
operation_var.set("encrypt")  # Default operation is encryption

ttk.Radiobutton(input_frame, text="Encrypt", variable=operation_var, value="encrypt").grid(row=2, column=0, sticky="w")
ttk.Radiobutton(input_frame, text="Decrypt", variable=operation_var, value="decrypt").grid(row=2, column=1, sticky="w")

# Button to send request
send_button = ttk.Button(input_frame, text="Process", command=send_request)
send_button.grid(row=3, columnspan=2, pady=20)

# Frame for displaying result
result_frame = ttk.Frame(root, padding="20")
result_frame.pack()

ttk.Label(result_frame, text="Original Message:").grid(row=0, column=0, sticky="w")
original_display = ttk.Label(result_frame, text="", wraplength=400)
original_display.grid(row=0, column=1, padx=10)

ttk.Label(result_frame, text="Processed Message:").grid(row=1, column=0, sticky="w")
processed_display = ttk.Label(result_frame, text="", wraplength=400)
processed_display.grid(row=1, column=1, padx=10)

result_var = tk.StringVar()

def update_result_display():
    original_display.config(text=message_entry.get())
    processed_display.config(text=result_var.get())

result_var.trace_add("write", lambda *args: update_result_display())

root.mainloop()
