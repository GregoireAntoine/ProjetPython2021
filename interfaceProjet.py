import tkinter as tk
from tkinter import messagebox
import os
import csv
from tkcalendar import *

    # ajouter un écran pour y mettre son nom et son mdp
def interface(Creator) : 
    try:
        with open("listing.csv", 'r') :
            print('ok')
    except FileNotFoundError :
        with open("listing.csv", 'a') :
            print("fichier créé")

    class evenement :
        def __init__(self, date, event, createur,acteurs):
            self.date = date
            self.event = event
            self.createur = createur
            self.acteurs=acteurs
        def enregistrement(self):
            with open('listing.csv','a',newline='', encoding='utf-8') as fichiercsv:
                if len(self.date)>4 :
                    writer=csv.writer(fichiercsv)
                    writer.writerow([self.date,self.event,self.createur,self.acteurs]) 
                else : messagebox.showinfo("Evenement", "Veuillez choisir une date")
                fichiercsv.close()
                print("Votre event a bien été enregistré !")
        
                
        def participants(self) : 
            partici=[]
            verif=0
            crea=""
            f= open (r"listing.csv")
            myReader = csv.reader(f)
            for row in myReader:
                if row[1]== self.event and row[0]==self.date :
                    crea=row[2]
                    partici.append([row[3]])
                    verif=1
            if verif!=1 :
                messagebox.showinfo("Votre evènement", "Créateur : "+crea +"\n"+"participants : aucuns")
                return False
            else :  
                messagebox.showinfo("Votre evènement", "Créateur : "+crea +"\n"+"participants : "+partici[0][0])
                return True        

        def suppresion(self) :
            calcul=0
            verif=0
            compteur=0
            eventtab=[]
            f= open (r"listing.csv")
            myReader = csv.reader(f)
            for row in myReader:
                eventtab.append([row[0],row[1],row[2],row[3]])
                verif=verif+1
            f.close()
            os.remove('listing.csv')
            with open('listing.csv','a',newline='', encoding='utf-8') as fichiercsv:
                while compteur < len(eventtab) :
                    if eventtab[compteur][1] != self.event or eventtab[compteur][0] != self.date : 
                        print(self.date)
                        print(eventtab[compteur][0])
                        writer=csv.writer(fichiercsv)
                        writer.writerow([eventtab[compteur][0],eventtab[compteur][1],eventtab[compteur][2],eventtab[compteur][3]]) 
                    else : 
                        calcul=1
                    compteur=compteur+1
                fichiercsv.close()
            if calcul==0 : 
                messagebox.showinfo("Votre evènement", "il n'y a pas d'évènement à suprimmer ")
                return False
            else :
                messagebox.showinfo("Votre evènement", "évènement bien supprimé ")
                return True

    fenetre = tk.Tk()
    fenetre.geometry("900x500") 

    def getEntry() :
        acteur=acteurs.get()
        ev = event.get()
        date=cal.get_date()
        activite = evenement(date,ev,Creator,acteur)
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
            activite = evenement(date,ev,Creator,acteurs)
            label=tk.Label(text=str(tableau[compteur][0]+" : "+tableau[compteur][1]),width=30)
            if verif != 0 :
                voirparticipant = tk.Button(fenetre, text='participants',command=lambda:activite.participants())
                voirparticipant.grid(row=4+compteur,column=2)
            if verif!=0 and Creator in tableau[compteur][2] : 
                labelbtn=tk.Button(text="supprimer", command=lambda : activite.suppresion())
                
                labelbtn.grid(row=4+compteur,column=3)
            label.grid(row=4+compteur,column=1)
            donnee=donnee+str(tableau[compteur][0]+" : "+tableau[compteur][1])+"\n"
            compteur=compteur+1
        
    def voir_tous_events():
        liste_event=[]
        lemessage=""
        verif=0
        crea=""
        f= open (r"listing.csv")
        myReader = csv.reader(f)
        for row in myReader:
            if row[2] == Creator or row[3] ==Creator :
                crea=row[2]
                liste_event.append([row[0],row[1],row[2],row[3]])
                verif=1
        if verif!=1 :
            messagebox.showinfo("event", "Vous n'avez pas d'event ")
            return False
        else : 
            compteur=0
            while compteur<len(liste_event)  : 
                lemessage=lemessage+"Créateur : "+crea +"\n"+ liste_event[compteur][0]+" : "+liste_event[compteur][1]+" avec "+liste_event[compteur][3]+"\n"
                compteur+=1
            messagebox.showinfo("Vos evènements", lemessage)
            return True


    def voirevent(date):
        eventtab=[]
        verif=0
        f= open (r"listing.csv")
        myReader = csv.reader(f)
        for row in myReader:
            if Creator in row[3] or Creator in row[2] :
                if date in row[0]:
                    eventtab.append([row[0],row[1],row[2],row[3]])
                    verif=verif+1
        if verif == 0 :
                eventtab.append([str(date),"pas d'événnements",Creator])
        
        affichage_event(eventtab,verif)


    
    valide = tk.Button(fenetre, text='validé',command=lambda:getEntry())
    titre=tk.Label(fenetre,text="calendrier")
    cal=Calendar(fenetre,selectmode='day',year=2020,month=5,)
    buttonAjout=tk.Label(fenetre,text="ajout event",width=35)
    buttonvoir=tk.Button(fenetre,text="voir event",width=35,command=lambda:voirevent(cal.get_date()))
    buttonvoirtoutevents=tk.Button(fenetre,text="voir tout les events",width=35,command=lambda:voir_tous_events())
    event = tk.Entry(fenetre)
    acteurs = tk.Entry(fenetre)

    titre.grid(row=0,column=1)
    buttonAjout.grid(row=3,column=0)
    buttonvoir.grid(row=1,column=1)
    buttonvoirtoutevents.grid(row=1,column=0)
    cal.grid(row=2,column=1)
    valide.grid(row=6,column=0)
    event.grid(row=4,column=0)
    acteurs.grid(row=5,column=0)
    fenetre.mainloop()