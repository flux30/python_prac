import tkinter as tk
from tkinter import messagebox

def perform_addition():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        result = num1 + num2
        messagebox.showinfo("Result", f"The sum is: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.title("Addition Form")

# Create labels and entry fields for two numbers
tk.Label(root, text="First Number:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
num1_entry = tk.Entry(root)
num1_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Second Number:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
num2_entry = tk.Entry(root)
num2_entry.grid(row=1, column=1, padx=5, pady=5)

# Create the Add button
add_button = tk.Button(root, text="Add", command=perform_addition)
add_button.grid(row=2, column=0, columnspan=2, pady=10)

# Run the GUI
root.mainloop()
