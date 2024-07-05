#Convert the Temperature one unit to second unit according to user requirement 
# program write my - Tushar Patel
#use VS code  editor and for GUI use tkinter


import tkinter as tk
from tkinter import messagebox
def convert():
    try:
        if var.get() == "Celsius to Fahrenheit":
            celsius = float(entry.get())
            fahrenheit = (celsius * 9/5) + 32
            result_label.config(text=f"{celsius} Celsius = {fahrenheit:.2f} Fahrenheit")
            
        elif var.get() == "Fahrenheit to Celsius":
            fahrenheit = float(entry.get())
            celsius = (fahrenheit - 32) * 5/9
            result_label.config(text=f"{fahrenheit} Fahrenheit = {celsius:.2f} Celsius")
            
        # More conversion cases for other units follow...
        
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid number.")
# Create the main window
root = tk.Tk()
root.title("Temperature Converter")

# Create GUI components
frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

label = tk.Label(frame, text="Enter temperature:")
label.grid(row=0, column=0, padx=10, pady=10)

entry = tk.Entry(frame)
entry.grid(row=0, column=1, padx=10, pady=10)

choices = ["Celsius to Fahrenheit", "Fahrenheit to Celsius",
           "Celsius to Kelvin", "Kelvin to Celsius",
           "Fahrenheit to Kelvin", "Kelvin to Fahrenheit"]

var = tk.StringVar(root)
var.set(choices[0])  # default value

dropdown = tk.OptionMenu(frame, var, *choices)
dropdown.grid(row=1, columnspan=2, padx=10, pady=10, sticky="ew")

convert_button = tk.Button(frame, text="Convert", command=convert)
convert_button.grid(row=2, columnspan=2, padx=10, pady=10)

result_label = tk.Label(frame, text="")
result_label.grid(row=3, columnspan=2, padx=10, pady=10)
root.mainloop()
