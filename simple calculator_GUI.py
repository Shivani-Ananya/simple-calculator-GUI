import tkinter as tk

def press(num):
    current = entry_var.get()
    entry_var.set(current + str(num))
    
def equalpress():
    try:
        total = str(eval(entry_var.get()))
        entry_var.set(total)
    except:
        entry_var.set("Error")
        
def clear():
    entry_var.set("")
    
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("360x420")
root.configure(bg = "#78B9B5")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=('Arial', 20), bd=10, insertwidth=2, width=14, borderwidth=4, bg="#FFF9BD", fg="black", justify='center')
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('/', 4, 3),
]

for (text, row, col) in buttons:
    if text == '=':
        action = equalpress
    elif text == 'C':
        action = clear
    else:
        action = lambda x=text: press(x)
        
    tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), bg="#FFF9E5", fg="black", command=action).grid(row=row, column=col, padx=5, pady=5)
root.mainloop()
