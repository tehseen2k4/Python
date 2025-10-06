
from tkinter import *
import math

def press(key):
    if key == '=':
        try:
            
            expression = entry.get()

            
            expression = expression.replace('sin', 'math.sin')
            expression = expression.replace('cos', 'math.cos')
            expression = expression.replace('tan', 'math.tan')
            expression = expression.replace('log', 'math.log10')
            expression = expression.replace('sqrt', 'math.sqrt')

           
            result = eval(expression)

           
            entry.delete(0, END)
            entry.insert(END, str(result))
        except Exception:
           
            entry.delete(0, END)
            entry.insert(END, "Error")

    elif key == 'Clr':
       
        entry.delete(0, END)
    else:
        
        entry.insert(END, key)


root = Tk()
root.title("🧮 Simple Calculator")
root.geometry("460x520")    
root.resizable(True, True)  


root.config(bg="#f5f5f5")

# --------------------------------------------------
# Entry field (Display screen)
# --------------------------------------------------
entry = Entry(
    root,
    font=('Consolas', 20),
    borderwidth=4,
    relief="ridge",
    justify="right",
    bg="#ffffff",
    fg="#000000"
)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20, ipady=10)


buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+'],
    ['sin', 'cos', 'tan', 'log'],
    ['sqrt', 'Clr']
]

for i, row in enumerate(buttons):
    for j, text in enumerate(row):
        Button(
            root,
            text=text,
            width=7,
            height=2,
            font=('Arial', 14, 'bold'),
            bg="#dfe6e9" if text != '=' else "#fdc728",  
            fg="#2d3436",
            activebackground="#fdc728",
            activeforeground="#000000",
            relief="raised",
            bd=2,
            command=lambda t=text: press(t)
        ).grid(row=i+1, column=j, padx=5, pady=5)

root.mainloop()
