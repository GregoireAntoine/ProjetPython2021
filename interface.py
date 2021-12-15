import tkinter  as tk
from tkinter.constants import DISABLED
from tkcalendar import *
from script import *

personne="GREG"


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

def getEntry() :
    ev = event.get()
    date=cal.get_date()
    enregistrement_event(str(date),str(ev)) 


def ajout_event(date) :

    valide = tk.Button(fenetre, text='validé', command= getEntry)
    frame_input.destroy()
    print(date)
    event.grid(row=3,column=1)
    valide.grid(row=4,column=1)
    



titre=tk.Label(fenetre,text="calendrier")
cal=Calendar(fenetre,selectmode='day',year=2020,month=5,)
buttonAjout=tk.Button(fenetre,text="ajout event",width=35,command=lambda : ajout_event(str(cal.get_date())))
buttonSupp=tk.Button(fenetre,text="supprimer event",width=35)
frame_input=tk.Label(fenetre,text="prochain evenement ")

titre.grid(row=0,column=1)
buttonAjout.grid(row=1,column=0)
buttonSupp.grid(row=1,column=2)
cal.grid(row=1,column=1)
frame_input.grid(row=4,column=1)



fenetre.mainloop()