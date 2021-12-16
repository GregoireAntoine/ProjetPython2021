import tkinter as tk
import csv

from Main import interface
def recupDonneConnexion(mdp, name ) : 
   f= open (r"Connexion.csv")
   myReader = csv.reader(f)
   for row in myReader:
       if mdp == row[0] and name == row[1] : 
           print("ok")
           return True
           

class utilisateur :
    def __init__(self, mdp,  createur):
        self.mdp = mdp
        self.createur = createur
    def connexion(self):
       if recupDonneConnexion(self.mdp,self.createur) == True :
           racine.destroy()
           interface(self.createur)
           return True
            
          
        #choper les données du csv et les comparés.
        

racine = tk.Tk()


def getEntry():
    name = nom.get()
    motdp =mdp.get()
    uti =utilisateur(motdp,name)
    uti.connexion()

nom= tk.Entry(racine, width=20)
nom.pack(pady=20)
mdp = tk.Entry(racine, width=20)
mdp.pack(pady=20)
btn = tk.Button(racine, height=1, width=10, text="connexion", command=getEntry)
btn.pack()

racine.mainloop()

# AJOUTER NOM AU DESSUS DES EMPLACEMENTS  MOT DE PASSE ET NOM 
# FAIRE EN SORTE QUE LORSQUE LA PERSONNE SE CONNECTE, CA ENVOIE LE NOM COMME CREATEUR ET CA OUVRE LE MAIN ET LE LANCE TOUT EN KILLANT LA FENETRE CONNEXION
#FAIRE LES TESTS.