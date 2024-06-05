import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import Font
from PIL import Image, ImageTk

path_img="C:\\xampp\\htdocs\\img\\ressources"

def create_digicode(parent_frame):
    solde = 10.0


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
            if solde != 0 :
                amount = float(amount_var.get())
                if solde >= amount:
                    solde -= amount
                    update_solde_label()
                    clear_amount()
                else: 
                    messagebox.showerror("Erreur", "Vous n'avez pas assez de d'argent sur votre solde")
            
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer un montant valide.")


    # Fonction pour retirer le dernier chiffre saisi
    def remove_digit():
        current_amount = amount_var.get()
        new_amount = current_amount[:-1]
        amount_var.set(new_amount)

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
        button = tk.Button(keypad_frame, text=text, command=lambda t=text: add_digit(t), font=("Courrier", 20), width=5, bg="#41B77F")
        button.grid(row=row, column=col, padx=5, pady=5)


    # Boutons fonctionnels
    zero_button = tk.Button(keypad_frame, text='0', command=lambda t='0': add_digit(t), font=("Courrier", 20), width=11,bg="#41B77F")
    zero_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)


    point_button = tk.Button(keypad_frame, text='.', command=add_point, font=("Courrier", 20), width=5, bg="#41B77F")
    point_button.grid(row=4, column=2, padx=5, pady=5)


    clear_button = tk.Button(keypad_frame, text='C', command=clear_amount, font=("Courrier", 20), width=5,  bg="#FFFF00")
    clear_button.grid(row=3, column=3, padx=5, pady=5)


    validation_icon = Image.open(path_img+"\\right.png")  # Assurez-vous de télécharger l'icône de validation sous le nom check_icon.png
    validation_icon = validation_icon.resize((40, 40), Image.BILINEAR)
    validation_icon = ImageTk.PhotoImage(validation_icon)
    valider_button = tk.Button(keypad_frame, image=validation_icon, command=confirm_amount, bd=2, width=85, height=50, bg="#00F000")
    valider_button.image= validation_icon
    valider_button.grid(row=4, column=3, padx=5, pady=5)

    effacer_icon = Image.open(path_img+"\\backspace.png")  # Assurez-vous de télécharger l'icône de validation sous le nom check_icon.png
    effacer_icon = effacer_icon.resize((40, 40), Image.BILINEAR)
    effacer_icon = ImageTk.PhotoImage(effacer_icon)
    effacer_button = tk.Button(keypad_frame, image=effacer_icon, command=remove_digit,bd=2, width=85,height=50, bg="#FF0000")
    effacer_button.image= effacer_icon
    effacer_button.grid(row=2, column=3, padx=5, pady=5)

    #verionjboheboijet