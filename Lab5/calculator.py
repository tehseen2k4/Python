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
root.title("Simple Calculator")
root.geometry("360x480")
root.resizable(False, False)
root.config(bg="#ececec")


entry = Entry(
    root,
    font=('Arial', 20),
    borderwidth=3,
    relief="sunken",
    justify="right",
    bg="white"
)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=15, ipady=8)


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
            width=8,
            height=2,
            font=('Arial', 13, 'bold'),
            bg="#f0f0f0" if text not in ('=', 'Clr') else ("#ffcb05" if text == '=' else "#ff6b6b"),
            fg="#000",
            bd=1,
            relief="ridge",
            command=lambda t=text: press(t)
        ).grid(row=i+1, column=j, padx=5, pady=5)

root.mainloop()
