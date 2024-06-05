import mysql.connector
import random
# Connexion à la base de données
db = mysql.connector.connect(
    host="localhost",
    user="admin",
    passwd="1234",
    database="serveur"
)

# Création d'un curseur pour exécuter des requêtes SQL
def creation_carte(ATR,Nom,Prenom,Age,num,RIB,img_URL,limite,solde,code):
    curseur = db.cursor()
    requete = "INSERT INTO membre (ATR,Nom,Prenom,Age,num,RIB,img_URL,limite,solde,code) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    curseur.execute(requete,(ATR,Nom,Prenom,Age,num,RIB,img_URL,limite,solde,code))
    db.commit()
    print(curseur.fetchone())
    curseur.close()
    
    
# creation_carte("123456719ABCDE","Dupont","Jean",30,"123456789","123456789","http://localhost/img/1.jpg",1000,1000,1234)

def afficher_solde(ATR):
    curseur = db.cursor()
    curseur.execute("SELECT solde FROM membre WHERE ATR = %s",(ATR,))
    solde = curseur.fetchone()[0]
    curseur.close()
    return solde

def pile_ou_face(choix):
    return choix==random.choice(["Pile","Face"])


def mise_argent(mise,choix,ATR):
    if afficher_solde(ATR)<mise:
        return -1
    if pile_ou_face(choix):
        recharge_solde(ATR,0.95*mise)
        return 0.95*mise
    else:
        recharge_solde(ATR,-mise)
        return 0
    
def recharge_solde(ATR,montant):
    curseur = db.cursor()
    curseur.execute("SELECT solde FROM membre WHERE ATR = %s",(ATR,))
    solde = curseur.fetchone()[0]
    curseur.execute("UPDATE membre SET solde = %s WHERE ATR = %s",(solde+montant,ATR))
    db.commit()
    curseur.close()

# recharge_solde("123456789ABCDE",100)
# print(mise_argent(100,"Pile","123456789ABCDE"))

def retire_argent(montant,ATR):
    if afficher_solde(ATR)<montant:
        return -1
    recharge_solde(ATR,-montant)
    return montant

def recuperation_donnees(ATR):
    curseur = db.cursor()
    curseur.execute("SELECT * FROM membre WHERE ATR = %s",(ATR,))
    donnees = curseur.fetchone()
    curseur.close()
    return donnees

def suppression_carte(ATR):
    curseur = db.cursor()
    curseur.execute("DELETE FROM membre WHERE ATR = %s",(ATR,))
    db.commit()
    curseur.close()

def lire_limite(ATR):
    curseur = db.cursor()
    curseur.execute("SELECT limite FROM membre WHERE ATR = %s",(ATR,))
    limite = curseur.fetchone()[0]
    curseur.close()
    return limite

def choisir_limite(ATR,limite):
    curseur = db.cursor()
    curseur.execute("UPDATE membre SET limite = %s WHERE ATR = %s",(limite,ATR))
    db.commit()
    curseur.close()

def choisir_code(ATR,code):
    curseur = db.cursor()
    curseur.execute("UPDATE membre SET code = %s WHERE ATR = %s",(code,ATR))
    db.commit()
    curseur.close()

# print(recuperation_donnees("123456789ABCDE"))
# ATR,Nom,Prenom,Age,num,RIB,img_URL,limite,solde,code = recuperation_donnees("123456789ABCDE")

# creation_carte("AE12123456789A",Nom,Prenom,Age,num,RIB,img_URL,limite,solde,code)