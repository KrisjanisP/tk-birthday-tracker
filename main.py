import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk
# from ttkthemes import ThemedTk
import os

if os.name == 'nt':  # 'nt' indicates Windows
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)

# root = ThemedTk(theme='adapta')
root = Tk()
root.title("My Birthday Tracker")
root.geometry('500x400')  # Set the window size
root.resizable(False, False)  # Disable resizing
style = ttk.Style(root)
style.theme_use("clam")  # Use the "clam" theme for a more modern look
# style.theme_use("adapta")  # Use the "clam" theme for a more modern look

tab_control = ttk.Notebook(root)
display_tab = ttk.Frame(tab_control)
add_tab = ttk.Frame(tab_control)

tab_control.add(display_tab, text="Display", padding=10)
tab_control.add(add_tab, text="Add birthday", padding=10)

tab_control.pack(expand=1, fill="both", padx=10, pady=10)

display_label = ttk.Label(display_tab, text="This is the display tab")
display_label.grid(column=0, row=0, pady=10, sticky="w")

ttk.Label(add_tab, text="This is the add tab").\
    grid(column=0, row=0, padx=30, pady=30)

listbox = tk.Listbox(display_tab, bd=0, highlightthickness=0)
listbox.grid(column=0, pady=10, row=1)
listbox.insert(tk.END, "Hello World")

ttk.Label(add_tab, text="Friend's Name:").\
grid(column=0, row=1, pady=5, sticky="w")
name_entry = ttk.Entry(add_tab)
name_entry.grid(column=1, row=1, pady=5, sticky="w")

ttk.Label(add_tab, text="Birthday (YYYY/MM/DD):").\
grid(column=0, row=2, pady=5, sticky="w")
birthday_entry = ttk.Entry(add_tab)
birthday_entry.grid(column=1, row=2, pady=5, sticky="w")


# Function to add a birthday to the list
def add_birthday():
    name = name_entry.get()
    birthday = birthday_entry.get()
    messagebox.showinfo("Success", "Birthday added successfully!")
    return
    if name and birthday:  # Check if the name and birthday fields are not empty
        # Load existing data
        with open(data_file, 'r') as file:
            birthdays = json.load(file)
        birthdays[name] = birthday
        # Save updated data
        with open(data_file, 'w') as file:
            json.dump(birthdays, file)
        messagebox.showinfo("Success", "Birthday added successfully!")
        name_entry.delete(0, tk.END)
        birthday_entry.delete(0, tk.END)
        refresh_listbox()
    else:
        messagebox.showerror("Error", "Name and birthday must be filled out")

add_button = ttk.Button(add_tab, text="Add Birthday", command=add_birthday)
add_button.grid(column=1, row=4, pady=20, sticky="e")


root.mainloop()