import tkinter as tk
from datetime import datetime as dt
import math
from time import sleep
num_files_encrypted = 10
# TODO encrypt 10 files immediately
last_click = dt.now()

def counter_label(label):
    def count():
        global num_files_encrypted
        global last_click
        time_left = math.ceil(3 - (dt.now() - last_click).total_seconds())
        if time_left < 0:
            time_left = 0
        label.config(text="Another file will be encrypted in " + str(time_left))
        if (dt.now()-last_click).total_seconds() > 3.0:
            num_files_encrypted += 1
            # TODO call encryption
            files_encrypted_label.config(text="encrypted " + str(num_files_encrypted) + " files")
        label.after(100, count)
    count()

def click():
    global last_click
    last_click = dt.now()

def surrender():
    # TODO ask for $10 amazon gift card
    pass

root = tk.Tk()
root.title("irritating-doggo.virus")
warning_label = tk.Label(root, fg="red", text="Closing this program will result in your files being lost forever")
warning_label.pack()
label = tk.Label(root, fg="red")
label.pack()
files_encrypted_label = tk.Label(root, fg="black", text="encrypted 10 files")
files_encrypted_label.pack()
counter_label(label)
# TODO make this invisible until 50 (or all) visible files are encrypted
button = tk.Button(root, text='Prevent Encryption', width=25, command=click)
button.pack()
button = tk.Button(root, text='I give up', width=25, command=click)
button.pack()
root.mainloop()