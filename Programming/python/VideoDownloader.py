import tkinter as tk
from tkinter import filedialog
import pytube

def download_video():
    video_url = url_entry.get()
    youtube = pytube.YouTube(video_url)
    
    streams = youtube.streams.filter(progressive=True)
    if not streams:
        status_label.configure(text="Error: no video streams available")
        return
    stream_menu_options = [str(stream.resolution) for stream in streams]
    
    stream_var.set(stream_menu_options[0])
    stream_menu = tk.OptionMenu(window, stream_var, *stream_menu_options)
    stream_menu.pack()
    
    def on_stream_selected(*args):
        selected_resolution = stream_var.get()
        selected_stream = next((stream for stream in streams if str(stream.resolution) == selected_resolution), None)
        if selected_stream is not None:
            download_dir = filedialog.askdirectory()
            if not download_dir:
                status_label.configure(text="Error: no download directory selected")
                return
            try:
                selected_stream.download(download_dir)
            except Exception as e:
                status_label.configure(text=f"Error: {str(e)}")
                return
            status_label.configure(text="Download complete!")
        else:
            status_label.configure(text="Error: selected stream not found")

    stream_var.trace("w", on_stream_selected)

window = tk.Tk()
window.title("Video Downloader")

url_label = tk.Label(window, text="Enter video URL:")
url_label.pack()
url_entry = tk.Entry(window)
url_entry.pack()

download_button = tk.Button(window, text="Download", command=download_video)
download_button.pack()

status_label = tk.Label(window, text="")
status_label.pack()

stream_var = tk.StringVar()

window.mainloop()