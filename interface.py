import tkinter  as tk
from tkinter import messagebox
from tkcalendar import *
from script import *
import time
personne="GREG"
try:
    with open("listing.csv", 'r') :
        print('ok')
except FileNotFoundError :
    with open("listing.csv", 'a') :
        print("fichier créé")


        
fenetre = tk.Tk()
fenetre.geometry("750x500")  


class evenement :
    def __init__(self, date, event, createur):
        self.date = date
        self.event = event
        self.createur = createur
    def ajout():
        print("ajout")
    
event = tk.Entry(fenetre)



compteurclass=0


def getEntry() :
    ev = event.get()
    date=cal.get_date()
    messagebox.showinfo("Votre evènement", "évènement bien enregistré ")
    acti=evenement(date,ev,"GREG")
    enregistrement_event(acti.date,acti.event)
    


def ajout_event(date) :
    valide = tk.Button(fenetre, text='validé', command=getEntry)
    valide.grid(row=3,column=0)
    event.grid(row=2,column=0)
    
   
    




def AffichageEvent ():
    LesEvents=voire_event(str(cal.get_date()))
    
    messagebox.showinfo("Votre evènement", "date : "+str(cal.get_date())+" : " +LesEvents[0][1]+"\n")




titre=tk.Label(fenetre,text="calendrier")
cal=Calendar(fenetre,selectmode='day',year=2020,month=5,)
buttonAjout=tk.Button(fenetre,text="ajout event",width=35,command=lambda : ajout_event(str(cal.get_date())))
buttonSupp=tk.Button(fenetre,text="supprimer event",width=35,command=lambda :supprimer() )
buttonvoir=tk.Button(fenetre,text="voir event",width=35,command=lambda :AffichageEvent() )


titre.grid(row=0,column=1)
buttonAjout.grid(row=1,column=0)
buttonvoir.grid(row=1,column=1)
buttonSupp.grid(row=1,column=2)
cal.grid(row=2,column=1)





def suppression(tableau, intitule):
    compteur=0
    with open('listing.csv','w',newline='', encoding='utf-8') as fichiercsv:      # on crée un nouveau fichier vierge
       writer=csv.writer(fichiercsv)
       while compteur<len(tableau) :      # on écrit toutes les données qui on été copiées dans le tableau et qui ne doivent pas être supprimées. 
         if tableau[compteur][2] != "GREG" and tableau[compteur][1] ==  intitule  : 
            writer.writerow([tableau[compteur][0],tableau[compteur][1],tableau[compteur][2]])
         compteur=compteur+1 
       fichiercsv.close()




def suppresion_boutons(tableau) :
    compteur=0
    while compteur< len(tableau) :
        activite=evenement(tableau[compteur][0], tableau[compteur][1], tableau[compteur][2])
        btnsup=Label(fenetre,text=activite.date+" : "+ activite.event, width=30)
        btnsup.grid(row=3+compteur,column=2)
        compteur=compteur+1

def supprimer () :
   tableau=[]                         #initalisation du tableau qui reprendra toutes les données
   f = open (r"listing.csv")           # récupération de toute les données
   myReader = csv.reader(f)
   for row in myReader:
      a=[row[0],row[1], row[2]]
      tableau.append(a)                   
   f.close() 
   os.remove('listing.csv')
   suppresion_boutons(tableau)            # on supprime le fichier qui contennait toutes les données
   


fenetre.mainloop()