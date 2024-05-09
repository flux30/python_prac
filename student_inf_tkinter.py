import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = name_entry.get()
    address = address_entry.get()
    class_level = class_entry.get()
    hobbies = hobbies_entry.get("1.0", tk.END)

    # Display the submitted information in a message box
    info = f"Name: {name}\nAddress: {address}\nClass: {class_level}\nHobbies: {hobbies}"
    messagebox.showinfo("Submitted Information", info)

def reset_form():
    name_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    class_entry.delete(0, tk.END)
    hobbies_entry.delete("1.0", tk.END)

# Create the main window
root = tk.Tk()
root.title("Student Information Form")

# Create labels and entry fields for name, address, class, and hobbies
tk.Label(root, text="Name:").grid(row=0, column=0, sticky="w")
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Address:").grid(row=1, column=0, sticky="w")
address_entry = tk.Entry(root)
address_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Class:").grid(row=2, column=0, sticky="w")
class_entry = tk.Entry(root)
class_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text="Hobbies:").grid(row=3, column=0, sticky="w")
hobbies_entry = tk.Text(root, height=4, width=30)
hobbies_entry.grid(row=3, column=1, padx=5, pady=5)

# Create Submit and Reset buttons
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=4, column=0, pady=10)

reset_button = tk.Button(root, text="Reset", command=reset_form)
reset_button.grid(row=4, column=1, pady=10)

# Run the GUI
root.mainloop()
