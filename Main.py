import tkinter as tk
import csv
from tkinter import messagebox
from interfaceProjet import interface

# interface de connexion au calendrier avec nom d'utilisateur et mot de passe
def connexion():
    def recupDonneConnexion(mdp, name ) : 
        f= open (r"Connexion.csv")
        myReader = csv.reader(f)
        for row in myReader:
            if mdp == row[0] and name == row[1] : 
                print("ok")
                return True
            
    # création de la class utilisateur
    class utilisateur :
        def __init__(self, mdp,  createur):
            self.mdp = mdp
            self.createur = createur
        def connexion(self):
            if recupDonneConnexion(self.mdp,self.createur) == True :
                racine.destroy()                                        # suppression de la fenêtre de connexion
                interface(self.createur)                                # ouverture de la fenêtre de calendrier avec le nom de l'utilisateur
                return True
                
            
            
            
    # initation de la fenêtre graphique de connexion
    racine = tk.Tk()

    # récupération des données inserez dans la page de connexion
    def getEntry():

        name = nom.get()
        motdp =mdp.get()
        if len(name)>=8 and len(motdp)>=8 :
            uti =utilisateur(motdp,name)
            uti.connexion()
        else : messagebox.showinfo("Connexion", "mot de passe et login doivent faire min 8 caractères ")
    # initiation des obejts graphique et placement dans la fenêtre graphique
    nom= tk.Entry(racine, width=20)
    nom.pack(pady=20)
    mdp = tk.Entry(racine,show="*", width=20)
    mdp.pack(pady=20)
    btn = tk.Button(racine, height=1, width=10, text="connexion", command=getEntry)
    btn.pack()

    racine.mainloop()


if __name__ == "__main__":
    connexion()