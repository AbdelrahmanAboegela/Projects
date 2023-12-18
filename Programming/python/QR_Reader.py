import cv2
from pyzbar import pyzbar
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image

class QRCodeScannerGUI:
    def __init__(self, master):
        self.master = master
        master.title("QR Code Scanner")

        self.frame = tk.Frame(master)
        self.frame.pack()

        self.image_label = tk.Label(self.frame)
        self.image_label.pack()

        self.result_label = tk.Label(self.frame, text="Scan a QR code")
        self.result_label.pack()

        self.choose_file_button = tk.Button(self.frame, text="Choose file", command=self.choose_file)
        self.choose_file_button.pack()

        self.camera_button = tk.Button(self.frame, text="Scan QR code from camera", command=self.scan_camera)
        self.camera_button.pack()

        self.quit_button = tk.Button(self.frame, text="Quit", command=self.quit)
        self.quit_button.pack()

    def choose_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        
        if file_path:
            try:
                img = cv2.imread(file_path)
                decoded_objects = pyzbar.decode(img)

                if decoded_objects:
                    for obj in decoded_objects:
                        self.result_label.config(text='QR code detected: {}'.format(obj.data.decode()))

                    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                    img = Image.fromarray(img)
                    img = ImageTk.PhotoImage(img)
                    self.image_label.config(image=img)
                    self.image_label.image = img
                else:
                    self.result_label.config(text='No QR code detected in the selected image')
            except:
                self.result_label.config(text='Error: Unable to process the selected image')

    def scan_camera(self):
        cap = cv2.VideoCapture(0)
        while True:
            _, frame = cap.read()
            decoded_objects = pyzbar.decode(frame)

            if decoded_objects:
                for obj in decoded_objects:
                    self.result_label.config(text='QR code detected: {}'.format(obj.data.decode()))

                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = Image.fromarray(frame)
                frame = ImageTk.PhotoImage(frame)
                self.image_label.config(image=frame)
                self.image_label.image = frame
                break

            cv2.imshow('QR Code Scanner', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    def quit(self):
        self.master.quit()

root = tk.Tk()
app = QRCodeScannerGUI(root)
root.mainloop()