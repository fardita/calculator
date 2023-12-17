import tkinter as tk
from tkinter import ttk

#Calcualtor operations
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def divide(n1, n2):
    if n2 != 0:
        return n1 / n2
    else:
        raise ValueError('do yuo want to divide for zero?'the result is INFINITE!)

def multiply(n1, n2):
    return n1 * n2

#Calculator function
def calculator(n1, n2, operation):
    operations = {
        'addition': add,
        'subtraction': subtract,
        'division': divide,
        'multiplication': multiply,
    }

    if operation in operations:
        return operations[operation](n1, n2)
    else:
        print('Invalid Operation')
        return None

#Create the GUI
def calculate():
    try:
        n1 = float(entry_n1.get())
        n2 = float(entry_n2.get())
    except ValueError:
        result_label.config(text="Invalid input", font=("Arial", 12, "bold"), foreground="red")
        return

    selected_operation = operation_var.get()

    try:
        result = calculator(n1, n2, selected_operation)
        if result is not None:
            result_label.config(text=f"Result: {result}", font=("Arial", 14), foreground="green")
    except ValueError as e:
        result_label.config(text=str(e), font=("Arial", 12, "bold"), foreground="red")

#Initialize the GUI
root = tk.Tk()
root.title("Calculator")

#Elements
entry_n1 = ttk.Entry(root, width=10)
entry_n2 = ttk.Entry(root, width=10)
operation_var = tk.StringVar()
operation_combobox = ttk.Combobox(root, textvariable=operation_var, values=['addition', 'subtraction', 'division', 'multiplication'])
calculate_button = ttk.Button(root, text="Calculate", command=calculate)
result_label = ttk.Label(root, text="Result: ", font=("Arial", 14))

#Layout
entry_n1.grid(row=0, column=0, padx=15, pady=30)
entry_n2.grid(row=0, column=1, padx=15, pady=15)
operation_combobox.grid(row=0, column=2, padx=15, pady=15)
calculate_button.grid(row=1, column=0, columnspan=3, pady=15)
result_label.grid(row=2, column=0, columnspan=3, pady=15)

# Run GUI
root.mainloop()
