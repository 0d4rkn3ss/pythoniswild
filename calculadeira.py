import tkinter as tk
from tkinter import messagebox
import re

def click(event):
    global expression
    text = event.widget.cget("text")
    if text == "=":
        try:
            sanitized_expression = re.sub(r'\b0+(\d)', r'\1', expression)
            result = eval(sanitized_expression)
            input_var.set(result)
            expression = str(result)
            entry.config(fg="green")
        except Exception as e:
            messagebox.showerror("Error", "Invalid Expression")
            expression = ""
            input_var.set("")
            entry.config(fg="red")
    elif text == "C":
        expression = ""
        input_var.set("")
        entry.config(fg="black")
    else:
        expression += text
        input_var.set(expression)
        entry.config(fg="black")

def on_enter(event):
    event.widget.config(bg="#d9d9d9")

def on_leave(event):
    button_text = event.widget.cget("text")
    original_color = button_colors.get(button_text, "#e6e6e6")
    event.widget.config(bg=original_color)

root = tk.Tk()
root.title("Calculadeira")
root.geometry("800x600")
root.resizable(True, True)
root.config(bg="#f0f0f0")

expression = ""
input_var = tk.StringVar()

entry = tk.Entry(
    root,
    textvar=input_var,
    font=("Arial", 24),
    justify="right",
    bd=10,
    relief=tk.SUNKEN,
    bg="#ffffff",
    fg="black"
)
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(expand=True, fill=tk.BOTH)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

button_colors = {
    "C": "#ff6666",
    "=": "#66ff66",
    "/": "#6699ff",
    "*": "#6699ff",
    "-": "#6699ff",
    "+": "#6699ff"
}

row, col = 0, 0
for button in buttons:
    color = button_colors.get(button, "#e6e6e6")
    btn = tk.Button(
        button_frame,
        text=button,
        font=("Arial", 18),
        relief=tk.RAISED,
        bd=5,
        bg=color,
        fg="black"
    )
    btn.grid(row=row, column=col, sticky="nsew", ipadx=10, ipady=10, padx=5, pady=5)
    btn.bind("<Button-1>", click)
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    col += 1
    if col > 3:
        col = 0
        row += 1

for i in range(4):
    button_frame.columnconfigure(i, weight=1)
for i in range(5):
    button_frame.rowconfigure(i, weight=1)

root.mainloop()