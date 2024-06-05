import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from Fonction_database import * 
path_img = "C:\\xampp\\htdocs\\img\\ressources"

# Fonction pour confirmer le montant et l'ajouter au solde




def create_digicode(parent_frame,type_opération,ATR):
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

    # Fonction pour obtenir le montant actuel et le passer à confirm_amount
    def get_amount():
        amount = amount_var.get()
        if type_opération == "retrait":
            retire_argent(ATR,amount)
        elif type_opération == "dépôt":
            recharge_solde(ATR,amount)
        elif type_opération == "limite":
            choisir_limite(ATR,amount)

    # Fonction pour retirer le dernier chiffre saisi
    def remove_digit():
        current_amount = amount_var.get()
        new_amount = current_amount[:-1]
        amount_var.set(new_amount)

    # Frame pour le pavé numérique
    keypad_frame = tk.Frame(parent_frame, bg="#008500")
    keypad_frame.grid(row=0, column=0, columnspan=3, sticky=(tk.W, tk.E))

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
        button = tk.Button(keypad_frame, text=text, command=lambda t=text: add_digit(t), font=("Courrier", 20), width=5, bg="#41B77F")
        button.grid(row=row, column=col, padx=5, pady=5)

    # Boutons fonctionnels
    zero_button = tk.Button(keypad_frame, text='0', command=lambda t='0': add_digit(t), font=("Courrier", 20), width=11, bg="#41B77F")
    zero_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    point_button = tk.Button(keypad_frame, text='.', command=add_point, font=("Courrier", 20), width=5, bg="#41B77F")
    point_button.grid(row=4, column=2, padx=5, pady=5)

    clear_button = tk.Button(keypad_frame, text='C', command=clear_amount, font=("Courrier", 20), width=5, bg="#FFFF00")
    clear_button.grid(row=3, column=3, padx=5, pady=5)

    validation_icon = Image.open(path_img + "\\right.png")
    validation_icon = validation_icon.resize((40, 40), Image.BILINEAR)
    validation_icon = ImageTk.PhotoImage(validation_icon)
    valider_button = tk.Button(keypad_frame, image=validation_icon, command=get_amount, bd=2, width=85, height=50, bg="#00F000")
    valider_button.image = validation_icon
    valider_button.grid(row=4, column=3, padx=5, pady=5)

    effacer_icon = Image.open(path_img + "\\backspace.png")
    effacer_icon = effacer_icon.resize((40, 40), Image.BILINEAR)
    effacer_icon = ImageTk.PhotoImage(effacer_icon)
    effacer_button = tk.Button(keypad_frame, image=effacer_icon, command=remove_digit, bd=2, width=85, height=50, bg="#FF0000")
    effacer_button.image = effacer_icon
    effacer_button.grid(row=2, column=3, padx=5, pady=5)

# # Exemple d'utilisation
# root = tk.Tk()
# root.title("Digicode")
# root.geometry("400x400")

# create_digicode(root)

# root.mainloop()
    