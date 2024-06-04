import mysql.connector
import urllib.request
from PIL import Image
from io import BytesIO

# Connexion à la base de données
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="test"
)

# Création d'un curseur pour exécuter des requêtes SQL
curseur = db.cursor()

# Demander à l'utilisateur d'entrer un ID
id_image = input("Entrez l'ID de l'image : ")

# Exécuter une requête SQL pour récupérer le chemin de l'image
chemin_image = "http://localhost/img/" + id_image + ".jpg"
print("Chemin de l'image :", chemin_image)

# Télécharger et afficher l'image
try:
    with urllib.request.urlopen(chemin_image) as url:
        image_data = url.read()
    image = Image.open(BytesIO(image_data))
    image.show()
except Exception as e:
    print("Erreur lors du téléchargement ou de l'affichage de l'image :", str(e))

# Fermeture du curseur et de la connexion à la base de données
curseur.close()
db.close()
