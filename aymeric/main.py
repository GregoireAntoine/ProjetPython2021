import tkinter as tk
from tkinter import messagebox
from tkcalendar import *
from utilisateur import Utilisateur

def clean_entry(entry):
    entry.delete('0', 'end')
    entry.insert('0', "")

class Gui:
    #Élément reprenant les tous ce que le popup Authentification
    def get_connexion_popup(self):
        self.auth_frame = tk.Tk()
        self.auth_frame.title("Authentification")
        self.auth_frame.geometry("500x400")
        lbl_user = tk.Label(self.auth_frame, text="Identifiant", height=1)
        lbl_password = tk.Label(self.auth_frame, text="Mot de passe", height=1)
        self.username_entry = tk.Entry(self.auth_frame, width=20)
        lbl_user.pack(pady=10)
        self.username_entry.pack()
        self.password_entry = tk.Entry(self.auth_frame, show="*", width=20)
        lbl_password.pack(pady=10)
        self.password_entry.pack()
        btn = tk.Button(self.auth_frame, height=1, width=10, text="Connexion", command=self.login)
        btn.pack(pady=10)
        btn_subscribe = tk.Button(self.auth_frame, height=1, width=10, text="S'inscrire", command=self.register)
        btn_subscribe.pack(pady=10)

    
    def btn_add_event(self, date):
        if not date:
            messagebox.showinfo("Ajouter évènement", "Veuillez sélectionner une date")
        elif not len(self.event_name.get()):
            messagebox.showinfo("Ajouter évènement", "Veuillez donner un nom à votre évènement")
        elif not len(self.event_acteurs.get()):
            messagebox.showinfo("Ajouter évènement", "Veuillez donner un nombre de participants à votre évènement")
        else:
            if self.user.events.event_already_exists(date, self.event_name.get()):
                messagebox.showinfo("Ajouter évènement", "L'évènement existe déjà")
            else:
                self.user.events.add_event(date, self.event_name.get(), self.event_acteurs.get())
                messagebox.showinfo("Ajouter évènement", "L'évènement a été ajouté")
                clean_entry(self.event_name)
                clean_entry(self.event_acteurs)
                self.btn_get_event_date(date)

    def print_list_events(self, events, org):
        # affiche l'ensemble des events 
        # clean
        ROW_START = 8
        COLUMN_START = 1
        for i in range(self.n_events):
            for j in range(3):
                widget = self.fenetre.grid_slaves(row=ROW_START + i, column=COLUMN_START + j)[0]
                if widget:
                    widget.grid_forget()
        if not len(events):
            label1 = tk.Label(text="Pas d'évènements", width=30)
            label2 = tk.Label(text=" ", width=30) # inutile mais pour le clean automatique
            label3 = tk.Label(text=" ", width=30) # inutile mais pour le clean automatique
            label1.grid(row=ROW_START, column=1)
            label2.grid(row=ROW_START, column=2)
            label3.grid(row=ROW_START, column=3)
            self.n_events = 1 # nombre de lignes à effacer
        else:
            for i, e in enumerate(events):
                label = tk.Label(text=f"{e[0]} : {e[1]}", width=30)
                label.grid(row=ROW_START + i, column= COLUMN_START)
                btn_view_acteurs = tk.Button(text="Participants", command=lambda: self.view_acteurs_event(e[0], e[1]))
                btn_view_acteurs.grid(row=ROW_START + i, column=COLUMN_START + 1)
                btn_remove_event = tk.Button(text="Supprimer", command=lambda: self.remove_event(e[0], e[1], org))
                btn_remove_event.grid(row=ROW_START + i, column=COLUMN_START + 2)
            self.n_events = len(events) # nombre de lignes à effacer

    def btn_get_event_date(self, date):
        if not date:
            messagebox.showinfo("Détail évènement", "Veuillez sélectionner une date")
        events = self.user.events.get_events_date(date)
        self.print_list_events(events, False)

    def btn_get_all_events(self):
        events = self.user.events.get_all_events()
        self.print_list_events(events, True)

    def view_acteurs_event(self, date, name):
        e = self.user.events.get_event(date, name)
        messagebox.showinfo("Détail évènement", f"Créateur = {e[2]}\nParticipants = {e[3]}")

    def remove_event(self, date, name, org):
        if self.user.events.remove_event(date, name) :
            messagebox.showinfo("Supprimer évènement", "L'évènement a été supprimé")
            if org: # org indique la vue à afficher en fonction de la vue d'origine : soit tous les events, soit les events d'un jour
                self.btn_get_all_events()
            else:
                self.btn_get_event_date(date)
        else:
            messagebox.showinfo("Supprimer évènement", "Vous ne pouvez pas supprimer un évènement dont vous n'êtes pas le créateur")

    def get_userframe(self):
        self.fenetre = tk.Tk("Mon Calendrier")
        self.fenetre.title("Mon Calendrier")
        self.fenetre.geometry("1000x500")
        self.n_events = 0
        cal = Calendar(self.fenetre, selectmode='day', year=2020, month=5, ) # date par défaut du calendrier

        # créations des objets graphiques présent à l'écran
        valid = tk.Button(self.fenetre, text='Valider', command=lambda:self.btn_add_event(cal.get_date()))
        titre = tk.Label(self.fenetre, text="Calendrier")
        label_event = tk.Label(self.fenetre, text="Ajout évènement", width=35)
        label_participant = tk.Label(self.fenetre, text="Participants", width=35)
        btn_get_event = tk.Button(self.fenetre, text="Voir évènement", width=35, command=lambda:self.btn_get_event_date(cal.get_date()))
        btn_get_all_events = tk.Button(self.fenetre, text="Voir tout les évènements", width=35, command=lambda:self.btn_get_all_events())
        self.event_name = tk.Entry(self.fenetre)
        self.event_acteurs = tk.Entry(self.fenetre)

        # Disposition des objets graphique dans la fenêtre
        titre.grid(row=0, column=1)
        btn_get_all_events.grid(row=1, column=0)
        self.event_name.grid(row=3, column=0)
        label_participant.grid(row=4, column=0)
        self.event_acteurs.grid(row=5, column=0)
        label_event.grid(row=2, column=0)
        valid.grid(row=6, column=0)
        btn_get_event.grid(row=1, column=1)
        cal.grid(row=2, column=1, rowspan=5)
        self.fenetre.mainloop()

    def check_credential(self, name, password):
        return len(name) >= 8 and len(password) >= 8
        #return True

    def login(self):
        name = self.username_entry.get().upper()
        password = self.password_entry.get()
        if self.check_credential(name, password):
            self.user = Utilisateur(name, password)
            if self.user.bind():
                self.auth_frame.destroy()
                self.get_userframe()
            else:  # probleme de connexion
                if self.user.username_exists():
                    messagebox.showinfo("Connexion", "Mauvais mot de passe")
                else:
                    messagebox.showinfo("Connexion", "Utilisateur inconnu")
        else:
            messagebox.showinfo("Connexion", "Mot de passe et login doivent faire min 8 caractères")

    def register(self):
        username = self.username_entry.get().upper()
        password = self.password_entry.get()
        if self.check_credential(username, password):
            self.user = Utilisateur(username, password)
            if self.user.create_user():
                self.auth_frame.destroy()
                self.get_userframe()
            else:
                messagebox.showinfo("Inscription", "Utilisateur déjà connu")
        else:
            messagebox.showinfo("Inscription", "Mot de passe et login doivent faire min 8 caractères")

    def __init__(self):
        self.get_connexion_popup()
        self.auth_frame.mainloop()


if __name__ == "__main__":
    g = Gui()
