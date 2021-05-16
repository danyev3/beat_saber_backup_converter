# Libraries OwO
from os import listdir, remove, path, chdir
import sys
from shutil import rmtree
from re import compile
import tkinter as tk
from tkinter import filedialog
from threading import *


# Changing the working directory to the temporary one created by pyinstaller (mainly for the .ico)
try:
    chdir(sys._MEIPASS)
except AttributeError:
    pass


# Name of the files to keep in the backup folder
files_to_keep = ["AvatarData.dat", "LocalDailyLeaderboards.dat", "LocalLeaderboards.dat", "PlayerData.dat", "settings.cfg", "AvatarData.dat.bak", "LocalDailyLeaderboards.dat.bak", "LocalLeaderboards.dat.bak", "PlayerData.dat.bak", "settings.cfg.bak"]


# Check if there's a Beat Saber backup in the directory
def is_backup(bk_dir):
    dir_files = listdir(bk_dir)
    is_bk = False
    for file in files_to_keep:
        if file in dir_files:
            is_bk = True
    if is_bk:
        btn_convert_backup["state"] = "normal"
        backup_found_txt.set("Beat Saber backup found!")
    else:
        btn_convert_backup["state"] = "disabled"
        backup_found_txt.set("Beat Saber backup not found")


# Open "Choose directory" window
def get_dir():
    # Open directory window
    sel_dir = filedialog.askdirectory()
    # Set selected dir in entry variable
    backup_dir.set(sel_dir)
    # Check if there's an actual directory selected
    if backup_dir.get() != "":
        # Enable the conversion button
        is_backup(backup_dir.get())
    else:
        # Disable the conversion button
        btn_convert_backup["state"] = "disabled"
        backup_found_txt.set("Beat Saber backup not found")


# Convert backup
def convert_backup():
    btn_path["state"] = "disabled"
    btn_convert_backup["state"] = "disabled"
    checkbox_old_form["state"] = "disabled"
    backup_found_txt.set("Converting...")
    dir_path = backup_dir.get()
    dir_files = listdir(dir_path)
    for file in dir_files:
        if file not in files_to_keep:
            file_path = f"{dir_path}/{file}"
            if path.isdir(file_path):
                rmtree(file_path)
            else:
                remove(file_path)
    for file in files_to_keep:
        try:
            with open(f"{dir_path}/{file}", "r") as _file:
                data = _file.read()
            pattern = compile("custom_level_(........................................)")
            custom_levels = pattern.findall(data)
            for level in custom_levels:
                if not convert_old_form.get():
                    data = data.replace(level, level.upper())
                else:
                    data = data.replace(level, level.lower())
            with open(f"{dir_path}/{file}", "w") as _file:
                _file.write(data)
        except FileNotFoundError:
            pass
    btn_path["state"] = "normal"
    checkbox_old_form["state"] = "normal"
    backup_found_txt.set("Backup converted!")


# Threads
def thread_get_dir():
    thread = Thread(target=get_dir)
    thread.start()


def thread_convert_backup():
    thread = Thread(target=convert_backup)
    thread.start()


# Let's make this damned GUI.
# There's a lot of weights and stuff cause the GUI was supposed to be resizable, then I realized idgaf about that
# Create the window and configure the grid
win = tk.Tk()
win.title("Beat Saber Backup Converter")
win.iconbitmap("icon.ico")
win.resizable(False, False)
win.rowconfigure(0, weight=0)
win.rowconfigure(1, weight=0)
win.rowconfigure(2, weight=1, minsize=75)
win.columnconfigure(0, weight=1, minsize=5)

# Cute growoy frame
frm = tk.Frame(master=win, relief=tk.GROOVE, borderwidth=3)
frm.columnconfigure(0, weight=1)
frm.columnconfigure(1, weight=2)
frm.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="we")
# Directory selection button
backup_dir = tk.StringVar()
btn_path = tk.Button(master=frm, text='Select the "files" backup folder', command=thread_get_dir)
btn_path.grid(row=0, rowspan=2, column=0, padx=5, pady=5, sticky="wens")
# Directory selection entry
path_ent = tk.Entry(master=frm, width=75, state='disabled', textvariable=backup_dir)
path_ent.grid(row=0, column=1, padx=5, pady=5)
# Song number labels
backup_found_txt = tk.StringVar(value=f"Beat Saber backup not found")
lbl_quest = tk.Label(master=frm, textvariable=backup_found_txt)
lbl_quest.grid(row=1, column=1, sticky="wens")

# Old format checkbox
convert_old_form = tk.BooleanVar(value=0)
checkbox_old_form = tk.Checkbutton(master=win, text="Convert to the old (1.13.2<) format instead of the new (1.13.4>) one (Don't use if you don't know what this is)", variable=convert_old_form, padx=10)
checkbox_old_form.grid(row=1, column=0, sticky="w")

# Conversion button
btn_convert_backup = tk.Button(master=win, text="Convert Backup", command=thread_convert_backup)
btn_convert_backup.grid(row=2, column=0, padx=5, pady=5, sticky="wens")
# Disable the conversion button
btn_convert_backup["state"] = "disabled"

# GUI LET'S GOOOOOOOOOO
win.mainloop()
