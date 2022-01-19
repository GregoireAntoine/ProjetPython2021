import tkinter as tk
import csv
from tkinter import messagebox
import os
from interfaceProjet import interface


class Utilisateur:
    FILE_NAME = 'Connexion.csv'

    def __init__(self, username, password):
        self.password = password
        self.username = username

    def bind(self):
        auth = False
        if os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME, 'r') as csvfile:
                csv_reader = csv.reader(csvfile)
                for row in csv_reader:
                    if len(row):
                        if self.username == row[0] and self.password == row[1]:
                            auth = True
        return auth

    def is_username_exists(self):
        exists = False
        if os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME, 'r') as csvfile:
                csv_reader = csv.reader(csvfile)
                for row in csv_reader:
                    if len(row):
                        if self.username == row[0]:
                            exists = True
        return exists

    def save(self):
        save = False
        if not self.bind() and not self.is_username_exists():
            if os.path.exists(self.FILE_NAME):
                with open(self.FILE_NAME, 'a') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([self.username, self.password])
                save = True
            else:
                with open(self.FILE_NAME, 'w') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([self.username, self.password])
                save = True
        return save


class Gui():
    def get_connexion_popup(self):
        self.racine = tk.Tk()
        self.racine.geometry("400x300")
        user = tk.Label(self.racine, text="identifiant", height=1)
        usermdp = tk.Label(self.racine, text="mot de passe", height=1)
        self.username_entry = tk.Entry(self.racine, width=20)
        user.pack(pady=10)
        self.username_entry.pack()
        self.password_entry = tk.Entry(self.racine, show="*", width=20)
        usermdp.pack(pady=10)
        self.password_entry.pack()
        btn = tk.Button(self.racine, height=1, width=10,
                        text="connexion", command=self.login)
        btn.pack(pady=10)
        inscription = tk.Button(
            self.racine, height=1, width=10, text="S'inscrire", command=self.get_register)
        inscription.pack(pady=10)

    def get_userframe(self):
        interface(self.user.username)
        # voir ce qu'il y a dans interface

    def check_credential(self, name, password):
        return len(name) >= 8 and len(password) >= 8
        #return True

    def login(self):
        name = self.username_entry.get().upper()
        password = self.password_entry.get()
        if self.check_credential(name, password):
            self.user = Utilisateur(name, password)
            if self.user.bind():
                self.racine.destroy()
                self.get_userframe()
            else:  # probleme de connexion
                if self.user.is_username_exists():
                    messagebox.showinfo("Connexion", "Mauvais mot de passe")
                else:
                    messagebox.showinfo("Connexion", "Utilisateur inconnu")
        else:
            messagebox.showinfo(
                "Connexion", "Mot de passe et login doivent faire min 8 caractères ")

    def get_register(self):
        username = self.username_entry.get().upper()
        password = self.password_entry.get()
        if self.check_credential(username, password):
            self.user = Utilisateur(username, password)
            if self.user.save():
                messagebox.showinfo(
                    "Connexion", "Bien inscrit !")
                self.racine.destroy()
                self.get_userframe()
            else:
                messagebox.showinfo(
                    "Connexion", "Utilisateur déjà utilisé !")

        else:
            messagebox.showinfo(
                "Inscription", "mot de passe et login doivent faire min 8 caractères")

    def __init__(self):
        self.get_connexion_popup()
        self.racine.mainloop()


if __name__ == "__main__":
    g = Gui()