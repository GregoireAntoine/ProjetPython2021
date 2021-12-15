import tkinter as tk
from tkinter import messagebox
import script
import os
import csv
from tkcalendar import *

try:
    with open("listing.csv", 'r') :
        print('ok')
except FileNotFoundError :
    with open("listing.csv", 'a') :
        print("fichier créé")

class evenement :
    def __init__(self, date, event, createur):
        self.date = date
        self.event = event
        self.createur = createur

    def enregistrement(self):
        with open('listing.csv','a',newline='', encoding='utf-8') as fichiercsv:
            writer=csv.writer(fichiercsv)
            writer.writerow([self.date,self.event,self.createur]) 
            fichiercsv.close()
            print("Votre event a bien été enregistré !")

    def suppresion(self) :
        print("2")
        verif=0
        compteur=0
        eventtab=[]
        f= open (r"listing.csv")
        myReader = csv.reader(f)
        for row in myReader:
            eventtab.append([row[0],row[1],row[2]])
            verif=verif+1
        print("3")
        f.close()
        os.remove('listing.csv')
        print("4")
        with open('listing.csv','a',newline='', encoding='utf-8') as fichiercsv:
            while compteur < len(eventtab) :
                
                if eventtab[compteur][1] != self.event : 
                    writer=csv.writer(fichiercsv)
                    writer.writerow([eventtab[compteur][0],eventtab[compteur][1],eventtab[compteur][2]]) 
                compteur=compteur+1
            fichiercsv.close()
        



        # récuperer la liste 
        # copier tout dans un tableau
        # entrer la date et event que on veut supprimer en gérant faute de frappe 
        # et tout ça avec des class.......

fenetre = tk.Tk()
fenetre.geometry("750x500") 

def getEntry() :
    ev = event.get()
    date=cal.get_date()
    activite = evenement(date,ev,"GREG")
    messagebox.showinfo("Votre evènement", "évènement bien enregistré ")
    activite.enregistrement()


  
def getsupprimerEntry() :
    ev = supprimer.get()
    date=cal.get_date()
    activite = evenement(date,ev,"GREG")
    print(ev)
    activite.suppresion()


def affichage_event(tableau) :
    compteur=0
    donnee=""
    while compteur<len(tableau): 
        donnee=donnee+str(tableau[compteur][0]+" : "+tableau[compteur][1])+"\n"
        compteur=compteur+1
    messagebox.showinfo("evènement", donnee)
    

def voirevent(date):
   eventtab=[]
   verif=0
   f= open (r"listing.csv")
   myReader = csv.reader(f)
   for row in myReader:
      if "GREG" in row[2] :
         if date in row[0]:
            eventtab.append([row[0],row[1],"GREG"])
            verif=verif+1
   if verif == 0 :
        eventtab.append([str(date),"pas d'événnements","GREG"])
   
   affichage_event(eventtab)


    
supprimer= tk.Entry(fenetre)
supprime = tk.Button(fenetre, text='supprimé',command=lambda:getsupprimerEntry())
valide = tk.Button(fenetre, text='validé',command=lambda:getEntry())
titre=tk.Label(fenetre,text="calendrier")
cal=Calendar(fenetre,selectmode='day',year=2020,month=5,)
buttonAjout=tk.Label(fenetre,text="ajout event",width=35)
buttonSupp=tk.Button(fenetre,text="supprimer event",width=35)
buttonvoir=tk.Button(fenetre,text="voir event",width=35,command=lambda:voirevent(cal.get_date()))
event = tk.Entry(fenetre)

titre.grid(row=0,column=1)
buttonAjout.grid(row=1,column=0)
buttonvoir.grid(row=1,column=1)
buttonSupp.grid(row=1,column=2)
cal.grid(row=2,column=1)
valide.grid(row=3,column=0)
event.grid(row=2,column=0)
supprimer.grid(row=2,column=2)
supprime.grid(row=3,column=2)
fenetre.mainloop()