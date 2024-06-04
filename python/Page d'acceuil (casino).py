from Interface import create_casino_home_page
from Fonction_database import *



ATR,Nom,Prenom,Age,num,RIB,img_URL,limite,solde,code=recuperation_donnees("123456789ABCDE")
create_casino_home_page("123456789ABCDE", Nom, Prenom, solde, limite, img_URL)