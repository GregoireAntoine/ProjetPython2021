import tkinter as tk
import csv
from tkinter import messagebox
from interfaceProjet import interface


def connexion():
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
        if len(name)>=8 and len(motdp)>=8 :
            uti =utilisateur(motdp,name)
            uti.connexion()
        else : messagebox.showinfo("Connexion", "mot de passe et login doivent faire min 8 caractères ")

    nom= tk.Entry(racine, width=20)
    nom.pack(pady=20)
    mdp = tk.Entry(racine,show="*", width=20)
    mdp.pack(pady=20)
    btn = tk.Button(racine, height=1, width=10, text="connexion", command=getEntry)
    btn.pack()

    racine.mainloop()


if __name__ == "__main__":
    connexion()