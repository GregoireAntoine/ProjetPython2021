import tkinter as tk
import csv
from tkinter import messagebox
from interfaceProjet import interface

FILE_NAME = 'Connexion.csv'

# interface de connexion au calendrier avec nom d'utilisateur et mot de passe
def connexion():
    # création de la class utilisateur
    class utilisateur :
        def __init__(self, mdp,  createur):
            self.mdp = mdp
            self.createur = createur
        def connexion(self):
            if self.recupDonneConnexion():
                racine.destroy()                                        # suppression de la fenêtre de connexion
                interface(self.createur)                                # ouverture de la fenêtre de calendrier avec le nom de l'utilisateur
                return True
            else :
                messagebox.showinfo("Inscription", "Cet identifiant existe déjà !")
            return False

        def recupDonneConnexion(self):
            auth = False
            f = open(FILE_NAME)
            myReader = csv.reader(f)
            for row in myReader:
                if self.mdp == row[0] and self.createur == row[1]:
                    auth = True
            return auth

        def add_donnee_connexion(self):
            if not self.recupDonneConnexion():
                with open(FILE_NAME, 'a', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([self.mdp, self.createur])
                messagebox.showinfo("Inscription", "Vous avez bien été inscrit !")
                racine.destroy()
                interface(self.createur)
            return True
                    
    # initation de la fenêtre graphique de connexion
    racine = tk.Tk()
    racine.geometry("400x300")
    # récupération des données inserez dans la page de connexion
    def getEntry():
        name = nom.get().upper()
        motdp =mdp.get()
        if len(name)>=8 and len(motdp)>=8 :
            uti =utilisateur(motdp,name)
            uti.connexion()
        else : 
            messagebox.showinfo("Connexion", "mot de passe et login doivent faire min 8 caractères")   

    def get_register():
        name = nom.get().upper()
        motdp = mdp.get()
        if len(name) >= 8 and len(motdp) >= 8:
            uti = utilisateur(motdp, name)
            uti.add_donnee_connexion()
        else:
            messagebox.showinfo("Inscription", "mot de passe et login doivent faire min 8 caractères")

    # initiation des obejts graphique et placement dans la fenêtre graphique
    user=tk.Label(racine,text="identifiant", height=1)
    usermdp=tk.Label(racine,text="mot de passe", height=1)
    nom= tk.Entry(racine, width=20)
    user.pack(pady=10)
    nom.pack()
    mdp = tk.Entry(racine,show="*", width=20)
    usermdp.pack(pady=10)
    mdp.pack()
    btn = tk.Button(racine, height=1, width=10, text="connexion", command=getEntry)
    btn.pack(pady=10)
    inscription = tk.Button(racine, height=1, width=10, text="S'inscrire", command=get_register)
    inscription.pack(pady=10)

    racine.mainloop()

if __name__ == "__main__":
    connexion()