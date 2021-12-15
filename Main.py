import tkinter as tk
from tkinter import messagebox
import script
import os
import csv
from tkcalendar import *

# ajouter un écran pour y mettre son nom et son mdp

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
        calcul=0
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
                else : 
                    calcul=1
                compteur=compteur+1
            fichiercsv.close()
        if calcul==0 : 
            messagebox.showinfo("Votre evènement", "il n'y a pas d'évènement à suprimmer ")
        else :
            messagebox.showinfo("Votre evènement", "évènement bien supprimé ")

fenetre = tk.Tk()
fenetre.geometry("750x500") 

def getEntry() :
    ev = event.get()
    date=cal.get_date()
    activite = evenement(date,ev,"GREG")
    messagebox.showinfo("Votre evènement", "évènement bien enregistré ")
    activite.enregistrement()





def affichage_event(tableau,verif) :
    valeuraffichage=0
    compteur=0
    donnee=""

    while valeuraffichage<20 :
        label=tk.Label(text="     ",width=30)
        label.grid(row=4+valeuraffichage,column=1)
        label1=tk.Label(text="     ",width=30,height=2)
        label1.grid(row=4+valeuraffichage,column=2)
        valeuraffichage+=1

    while compteur<len(tableau): 
        
        ev = tableau[compteur][1]
        date=cal.get_date()
        activite = evenement(date,ev,"GREG")
        label=tk.Label(text=str(tableau[compteur][0]+" : "+tableau[compteur][1]),width=30)
        if verif!=0 : 
            labelbtn=tk.Button(text="supprimer", command=lambda : activite.suppresion())
            labelbtn.grid(row=4+compteur,column=2)
        label.grid(row=4+compteur,column=1)
        donnee=donnee+str(tableau[compteur][0]+" : "+tableau[compteur][1])+"\n"
        compteur=compteur+1
    

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
   
   affichage_event(eventtab,verif)


 
valide = tk.Button(fenetre, text='validé',command=lambda:getEntry())
titre=tk.Label(fenetre,text="calendrier")
cal=Calendar(fenetre,selectmode='day',year=2020,month=5,)
buttonAjout=tk.Label(fenetre,text="ajout event",width=35)
buttonvoir=tk.Button(fenetre,text="voir event",width=35,command=lambda:voirevent(cal.get_date()))
event = tk.Entry(fenetre)

titre.grid(row=0,column=1)
buttonAjout.grid(row=1,column=0)
buttonvoir.grid(row=1,column=1)
cal.grid(row=2,column=1)
valide.grid(row=3,column=0)
event.grid(row=2,column=0)

fenetre.mainloop()