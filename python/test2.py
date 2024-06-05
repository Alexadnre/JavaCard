import tkinter as tk

root = tk.Tk()

# Créer un widget au-dessus de l'espaceur
button = tk.Button(root, text="Click Me")
button.pack()

# Créer un espaceur avec une couleur de fond
spacer = tk.Frame(root, height=20, bg='red')
spacer.pack(fill='x')

# Créer un widget en dessous de l'espaceur
label = tk.Label(root, text="Hello, World!")
label.pack()

root.mainloop()