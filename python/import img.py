import mysql.connector
from PIL import Image

# Ouvrir l'image à insérer
image = Image.open("C:\\Users\\alexa\\OneDrive\\Images\\Pellicule\\alex.jpg")

# Convertir l'image en données binaires
with open("C:\\Users\\alexa\\OneDrive\\Images\\Pellicule\\alex.jpg", "rb") as fichier:
    donnees_image = fichier.read()

# Connexion à la base de données
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="test"
)

# Création d'un curseur pour exécuter des requêtes SQL
curseur = db.cursor()

# Rechercher l'ID de l'enregistrement correspondant à la personne nommée "Alexandre"
requete_id = "SELECT ID FROM bouh WHERE Prenom = %s"
nom_personne = "Alexandre"
curseur.execute(requete_id, (nom_personne,))
resultat_id = curseur.fetchone()

# Vérifier si l'enregistrement a été trouvé
if resultat_id:
    id_personne = resultat_id[0]
    
    # Insérer l'image dans la base de données avec l'ID de la personne
    requete_insertion = "UPDATE bouh SET photo = %s WHERE ID = %s"
    donnees_insertion = (donnees_image, id_personne)
    curseur.execute(requete_insertion, donnees_insertion)
    db.commit()
    
    print("L'image a été insérée pour la personne nommée", nom_personne, "avec l'ID", id_personne)
else:
    print("Aucun enregistrement trouvé pour la personne nommée", nom_personne)

# Fermeture du curseur et de la connexion à la base de données
curseur.close()
db.close()
