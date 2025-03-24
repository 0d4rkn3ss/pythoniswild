import tkinter as tk
from tkinter import messagebox
import re

def click(event):
    """Handles button clicks."""
    global expression
    text = event.widget.cget("text")
    if text == "=":
        try:
            # Sanitize the expression by removing leading zeros from numbers
            sanitized_expression = re.sub(r'\b0+(\d)', r'\1', expression)
            result = eval(sanitized_expression)
            input_var.set(result)
            expression = str(result)
            entry.config(fg="green")  # Ai zeferino, que trabalheira que isto me deu no debug. Nunca mais.
        except Exception as e:
            messagebox.showerror("Error", "Invalid Expression")
            expression = ""
            input_var.set("")
            entry.config(fg="red")  # Change text color to red for errors
    elif text == "C":
        expression = ""
        input_var.set("")
        entry.config(fg="black")  # Preto do cara-
    else:
        expression += text
        input_var.set(expression)
        entry.config(fg="black")  # Preto de novo. Porra. Odeio. Odeio. Odeio.

def on_enter(event):
    """Change button color on hover."""
    event.widget.config(bg="#d9d9d9")  # Light gray on hover

def on_leave(event):
    """Revert button color when hover ends."""
    button_text = event.widget.cget("text")
    original_color = button_colors.get(button_text, "#e6e6e6")  # Default light gray
    event.widget.config(bg=original_color)

# Se isto falha, queima a casa toda. E eu não tenho seguro. E o meu gato morre. E eu fico sem gato. E eu gosto do meu gato. Bem merda.
root = tk.Tk()
root.title("Calculadeira")
root.geometry("800x600")  # Default size
root.resizable(True, True)  # Allow resizing
root.config(bg="#f0f0f0")  # Set background color

# Global variables for the win. Ou então não. Mas é o que temos. E é o que vamos usar. E é o que vamos fazer. E é o que vamos ter. E é o que vamos ser. Devia ir para um hospital psiquiátrico.
expression = ""
input_var = tk.StringVar()

# Falha isto, falha tudo. Deus queira que não. Se falhar também não me importo. Já estou farto disto.
entry = tk.Entry(
    root,
    textvar=input_var,
    font=("Arial", 24),
    justify="right",
    bd=10,
    relief=tk.SUNKEN,
    bg="#ffffff",  # Por alma de quem é que pus metade em hex e metade em RGB? Estupidez.
    fg="black"  # Black text
)
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

# Podia ser melhor? Sim. Mas não é. E não vai ser. E não quero. E não vou. E não posso. E não devo. E não consigo.
button_frame = tk.Frame(root, bg="#f0f0f0")  # PORRA DO BACKGROUND COLOR QUE NÃO MUDA NEM POR NADA
button_frame.pack(expand=True, fill=tk.BOTH)

# Dark mode? Querias. Não tens. E não vais ter.
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

# Button colors, carvão. Que trabalheira. Hex é mesmo dificílimo.
button_colors = {
    "C": "#ff6666",  # Red for clear
    "=": "#66ff66",  # Green for equals
    "/": "#6699ff",  # Blue for operators
    "*": "#6699ff",
    "-": "#6699ff",
    "+": "#6699ff"
}

# Lá vamos nós com os malditos botões. Que trabalheira. E não é CSS.
row, col = 0, 0
for button in buttons:
    color = button_colors.get(button, "#e6e6e6")  # Default light gray for numbers
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
    btn.bind("<Enter>", on_enter)  # Bind hover start
    btn.bind("<Leave>", on_leave)  # Bind hover end
    col += 1
    if col > 3:
        col = 0
        row += 1

# Que moca linda. Qualquer dia isto queima o meu processador.
for i in range(4):  # 4 columns
    button_frame.columnconfigure(i, weight=1)
for i in range(5):  # 5 rows
    button_frame.rowconfigure(i, weight=1)

# Run Forrest, run!
root.mainloop()