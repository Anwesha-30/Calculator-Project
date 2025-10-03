import tkinter as tk

# Function to evaluate the expression
def press(key):
    entry.insert(tk.END, key)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)  # evaluates the entered expression
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

# Entry box
entry = tk.Entry(root, width=20, font=('Arial', 18), bd=5, relief=tk.RIDGE, justify='right')
entry.grid(row=0, column=0, columnspan=4, pady=10)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

# Create buttons
for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, width=5, height=2, font=('Arial', 14), command=calculate)
    else:
        btn = tk.Button(root, text=text, width=5, height=2, font=('Arial', 14), command=lambda t=text: press(t))
    btn.grid(row=row, column=col, padx=5, pady=5)

# Clear button
clear_btn = tk.Button(root, text="C", width=22, height=2, font=('Arial', 14), command=clear)
clear_btn.grid(row=5, column=0, columnspan=4, pady=5)

# Run the app
root.mainloop()
