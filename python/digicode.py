import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def create_digicode(parent_frame):
    solde = 0.0

    # Fonction pour mettre à jour l'affichage du solde
    def update_solde_label():
        solde_label.config(text=f"Solde: {solde:.2f} €")

    # Fonction pour ajouter un chiffre au montant
    def add_digit(digit):
        current_amount = amount_var.get()
        new_amount = current_amount + digit
        amount_var.set(new_amount)

    # Fonction pour ajouter un point décimal
    def add_point():
        current_amount = amount_var.get()
        if '.' not in current_amount:
            new_amount = current_amount + '.'
            amount_var.set(new_amount)

    # Fonction pour effacer le montant
    def clear_amount():
        amount_var.set('')

    # Fonction pour confirmer le montant et l'ajouter au solde
    def confirm_amount():
        nonlocal solde
        try:
            amount = float(amount_var.get())
            solde += amount
            update_solde_label()
            clear_amount()
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer un montant valide.")

    # Fonction pour retirer le dernier chiffre saisi
    def remove_digit():
        current_amount = amount_var.get()
        new_amount = current_amount[:-1]
        amount_var.set(new_amount)

    # Frame pour le solde
    solde_frame = tk.Frame(parent_frame, bg="#008500")
    solde_frame.grid(row=0, column=0, columnspan=3, pady=10, sticky=(tk.W, tk.E))

    solde_label = tk.Label(solde_frame, text=f"Solde: {solde:.2f} €", font=("Courrier", 20), bg="#008500", fg="white")
    solde_label.pack()

    # Frame pour le pavé numérique
    keypad_frame = tk.Frame(parent_frame, bg="#008500")
    keypad_frame.grid(row=1, column=0, columnspan=3, pady=10, sticky=(tk.W, tk.E))

    amount_var = tk.StringVar()

    amount_entry = tk.Entry(keypad_frame, textvariable=amount_var, font=("Courrier", 20), justify='center', width=10)
    amount_entry.grid(row=0, column=0, columnspan=3, pady=10)

    # Boutons numériques
    buttons = [
        ('1', 1, 0), ('2', 1, 1), ('3', 1, 2),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
        ('7', 3, 0), ('8', 3, 1), ('9', 3, 2)
    ]

    for (text, row, col) in buttons:
        button = tk.Button(keypad_frame, text=text, command=lambda t=text: add_digit(t), font=("Courrier", 20), width=5)
        button.grid(row=row, column=col, padx=5, pady=5)

    # Boutons fonctionnels
    zero_button = tk.Button(keypad_frame, text='0', command=lambda t='0': add_digit(t), font=("Courrier", 20), width=11)
    zero_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    point_button = tk.Button(keypad_frame, text='.', command=add_point, font=("Courrier", 20), width=5)
    point_button.grid(row=4, column=2, padx=5, pady=5)

    clear_button = tk.Button(keypad_frame, text='C', command=clear_amount, font=("Courrier", 20), width=5)
    clear_button.grid(row=3, column=3, padx=5, pady=5)

    valider_button = tk.Button(keypad_frame, text='V', command=confirm_amount, font=("Courrier", 20), width=5, bg="#AAFF50", fg="black")
    valider_button.grid(row=4, column=3, padx=5, pady=5)

    effacer_button = tk.Button(keypad_frame, text='E', command=remove_digit, font=("Courrier", 20), width=5, bg="#AAFF50", fg="black")
    effacer_button.grid(row=2, column=3, padx=5, pady=5)
