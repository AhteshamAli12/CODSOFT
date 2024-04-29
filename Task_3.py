import string
import random
import tkinter as tk
from tkinter import messagebox

def password_generate(length, a):
    if a == 1:
        num = string.digits
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        punct = string.punctuation
        combine  = num + lower + upper + punct

        random_pass = random.sample(combine, length)
        random_pass = "".join(random_pass)
        return random_pass
    elif a == 2:
        num = string.digits
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        combine  = num + lower + upper

        random_pass = random.sample(combine, length)
        random_pass = "".join(random_pass)
        return random_pass
    elif a == 3:
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        punct = string.punctuation
        combine  = lower + upper + punct

        random_pass = random.sample(combine, length)
        random_pass = "".join(random_pass)
        return random_pass
    elif a == 4:
        num = string.digits
        punct = string.punctuation
        combine  = num + punct

        random_pass = random.sample(combine, length)
        random_pass = "".join(random_pass)
        return random_pass

def create_gui():
    def generate_password():
        try:
            complexity = int(complexity_var.get())
            length = int(length_entry.get())
            if 1 <= complexity <= 4 and length > 0:
                password = password_generate(length, complexity)
                password_label.config(text=f"Random password generated: {password}")
            else:
                messagebox.showerror("Error", "Invalid Complexity or Length")
        except ValueError:
            messagebox.showerror("Error", "Invalid Complexity or Length")

    root = tk.Tk()
    root.title("Random Password Generator")

    complexity_label = tk.Label(root, text="Select the complexity of password:")
    complexity_label.pack()

    complexity_var = tk.IntVar()
    complexity_options = [("Alphabet + Numeric + Symbols", 1),
                          ("Alphabet + Numeric", 2),
                          ("Alphabet + Symbols", 3),
                          ("Numeric + Symbols", 4)]
    for text, val in complexity_options:
        tk.Radiobutton(root, text=text, variable=complexity_var, value=val).pack()

    length_label = tk.Label(root, text="Enter the length of password:")
    length_label.pack()

    length_entry = tk.Entry(root)
    length_entry.pack()

    generate_button = tk.Button(root, text="Generate Password", command=generate_password)
    generate_button.pack()

    password_label = tk.Label(root, text="")
    password_label.pack()

    root.mainloop()

create_gui()
