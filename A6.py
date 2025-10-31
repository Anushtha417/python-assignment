from tkinter import *

# Window setup
root = Tk()
root.title("Calculator")

# Entry widget
entry = Entry(root, width=35, borderwidth=5, font=('Arial', 18))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button Click Function
def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))

def button_clear():
    entry.delete(0, END)

def button_add():
    global f_num, operation
    f_num = float(entry.get())
    operation = "add"
    entry.delete(0, END)

def button_subtract():
    global f_num, operation
    f_num = float(entry.get())
    operation = "sub"
    entry.delete(0, END)

def button_multiply():
    global f_num, operation
    f_num = float(entry.get())
    operation = "mul"
    entry.delete(0, END)

def button_divide():
    global f_num, operation
    f_num = float(entry.get())
    operation = "div"
    entry.delete(0, END)

def button_equal():
    s_num = float(entry.get())
    entry.delete(0, END)

    if operation == "add":
        entry.insert(0, f_num + s_num)
    elif operation == "sub":
        entry.insert(0, f_num - s_num)
    elif operation == "mul":
        entry.insert(0, f_num * s_num)
    elif operation == "div":
        entry.insert(0, f_num / s_num)

# Buttons
buttons = [
    ("7", lambda: button_click(7)), ("8", lambda: button_click(8)), ("9", lambda: button_click(9)), ("/", button_divide),
    ("4", lambda: button_click(4)), ("5", lambda: button_click(5)), ("6", lambda: button_click(6)), ("*", button_multiply),
    ("1", lambda: button_click(1)), ("2", lambda: button_click(2)), ("3", lambda: button_click(3)), ("-", button_subtract),
    ("C", button_clear), ("0", lambda: button_click(0)), ("=", button_equal), ("+", button_add)
]

# Place buttons on grid
row_val = 1
col_val = 0

for text, cmd in buttons:
    Button(root, text=text, padx=20, pady=20, font=('Arial', 14), command=cmd).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val == 4:
        row_val += 1
        col_val = 0

root.mainloop()
