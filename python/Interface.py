import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from io import BytesIO
import urllib.request
from Fonction_database import *
from digicode import *

def create_casino_home_page(ATR, Nom, Prenom, solde, limite, img_URL):
    # Create the main window
    root = tk.Tk()
    root.title("Casino Home Page")

    # Set window aspect ratio to 16:9
    root.geometry("1280x720")

    # Define the main frame
    main_frame = ttk.Frame(root, padding="10")
    main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    # Add a background color to visualize the grid
    for i in range(7):
        for j in range(6):
            cell = tk.Label(main_frame, text='', bg='#008500', borderwidth=1, relief="solid", width=20, height=5)
            cell.grid(row=i, column=j, sticky=(tk.W, tk.E, tk.N, tk.S))

     # Load and display the photo
    response = urllib.request.urlopen(img_URL)
    image = Image.open(response)
    image = image.resize((200, 200))  # Resize the image to fit the placeholder
    photo = ImageTk.PhotoImage(image)

    photo_label = tk.Label(main_frame, image=photo, relief="solid", width=200, height=200)
    photo_label.image = photo  # Keep a reference to the image to prevent garbage collection
    photo_label.grid(row=0, column=5, rowspan=2, padx=5, pady=5) 

    # User information
    ttk.Label(main_frame, text="ATR: " + ATR).grid(row=6, column=0, sticky=tk.W)

    Nom_label = ttk.Label(main_frame, text=Nom,font=("Helvetica", 16, "bold"))
    Nom_label.grid(row=0, column=0, padx=5)

    firstNom_label = ttk.Label(main_frame, text=Prenom)
    firstNom_label.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=5)

    # solde information
    ttk.Label(main_frame, text="Solde: " + str(solde)).grid(row=2, column=2, columnspan=2, sticky=(tk.W, tk.E))

    # Action buttons
    deposit_button = ttk.Button(main_frame, text="Déposer")
    deposit_button.grid(row=3, column=2, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5, pady=5)

    withdraw_button = ttk.Button(main_frame, text="Retirer")
    withdraw_button.grid(row=3, column=3, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5, pady=5)

    renew_button = ttk.Button(main_frame, text="Renouvellement")
    renew_button.grid(row=4, column=2, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5, pady=5)

    # limite information
    limite_button = ttk.Button(main_frame, text="limite")
    limite_button.grid(row=4, column=3, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5, pady=5)

    ttk.Label(main_frame, text=f"limite actuelle: {str(limite)}").grid(row=6, column=5, columnspan=2, sticky=tk.W)
    ttk.Label(main_frame,)
    # Configure column and row weights for proper resizing
    for i in range(6):
        main_frame.columnconfigure(i, weight=1)
    for i in range(8):
        main_frame.rowconfigure(i, weight=1)

    # Run the application
    root.mainloop()


def digicode(ATR, Nom, Prenom, solde, limite, img_URL):
    # Create the main window
    root = tk.Tk()
    root.title("Casino Home Page")

    # Set window aspect ratio to 16:9
    root.geometry("1280x720")

    # Define the main frame
    main_frame = ttk.Frame(root, padding="10")
    main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    # Add a background color to visualize the grid
    for i in range(7):
        for j in range(6):
            cell = tk.Label(main_frame, text='', bg='#008500', borderwidth=1, relief="solid", width=20, height=5)
            cell.grid(row=i, column=j, sticky=(tk.W, tk.E, tk.N, tk.S))

    # User information
    ttk.Label(main_frame, text="ATR: " + ATR).grid(row=6, column=0, sticky=tk.W)

    Nom_label = ttk.Label(main_frame, text=Nom,font=("Helvetica", 16, "bold"))
    Nom_label.grid(row=0, column=0, padx=5)

    firstNom_label = ttk.Label(main_frame, text=Prenom)
    firstNom_label.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=5)


    #intégration digicode

    digicode_frame = ttk.Label(main_frame, text="digicode")
    digicode_frame.grid(row=2, column=2, columnspan=2, rowspan=3, sticky=(tk.W, tk.E))

    # Créer le pavé numérique dans le digicode_frame
    create_digicode(digicode_frame)


    # Configure column and row weights for proper resizing
    for i in range(6):
        main_frame.columnconfigure(i, weight=1)
    for i in range(8):
        main_frame.rowconfigure(i, weight=1)

    # Run the application
    root.mainloop()



ATR,Nom,Prenom,Age,num,RIB,img_URL,limite,solde,code=recuperation_donnees("123456789ABCDE")
create_casino_home_page("123456789ABCDE", Nom, Prenom, solde, limite, img_URL)