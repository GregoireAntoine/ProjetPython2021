from tkinter import *
import os
import tkinter as tk
import csv
from tkinter import messagebox
from interfaceProjet import interface

# interface de connexion au calendrier avec nom d'utilisateur et mot de passe
def connexion():
    def recupDonneConnexion(mdp, name ) : 
        f= open ("Connexion.csv")
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
    racine.geometry("300x200")
    # récupération des données inserez dans la page de connexion
    def getEntry():

        name = nom.get().upper()
        motdp =mdp.get()
        if len(name)>=8 and len(motdp)>=8 :
            uti =utilisateur(motdp,name)
            uti.connexion()
        else : messagebox.showinfo("Connexion", "mot de passe et login doivent faire min 8 caractères ")
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
    inscription = tk.Button(racine, height=1, width=10, text="S'inscrire", command=getEntry)
    inscription.pack(pady=10)

    racine.mainloop()

if __name__ == "__main__":
    connexion()


def dernierevent():
   presenceevent = 0
   compteur = 0
   tableau = []
   f = open(r"listing.csv")
   myReader = csv.reader(f)
   for row in myReader:
      if "GREG" in row[2]:
         tableau.append(row[0] + row[1])
         compteur = compteur+1
         presenceevent = presenceevent+1

   return tableau[len(tableau)-1]


def enregistrement_event(date, event):
   with open('listing.csv', 'a', newline='', encoding='utf-8') as fichiercsv:
       writer = csv.writer(fichiercsv)
       writer.writerow([date, event, "GREG"])
       fichiercsv.close()
       print("Votre event a bien été enregistré !")


def voire_event(date):
   verif = 0
   eventtab = []
   f = open(r"listing.csv")
   myReader = csv.reader(f)
   for row in myReader:
      if "GREG" in row[2]:
         if date in row[0]:
            eventtab.append([row[0], row[1], "GREG"])
            verif = verif+1
   if verif == 0:
        eventtab.append(['0', "pas d'événnements","GREG"])
   return eventtab
