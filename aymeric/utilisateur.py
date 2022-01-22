import os
import csv
from evenement import Evenements


class Utilisateur :
    FILE_NAME = 'Connexion.csv'
    
    def __init__(self, username, password):
        self.password = password
        self.username = username
        self.events = Evenements(self.username)
        
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

    def username_exists(self):
        exists = False
        if os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME, 'r') as csvfile:
                csv_reader = csv.reader(csvfile)
                for row in csv_reader:
                    if len(row):

                        print(row[0], "?", self.username)
                        if self.username == row[0]:
                            exists = True
        return exists

    def save(self):
        save = False
        if not self.bind() and not self.username_exists():
            if os.path.exists(self.FILE_NAME):
                with open(self.FILE_NAME, 'a', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([self.username, self.password])
                save = True
            else:
                with open(self.FILE_NAME, 'w', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([self.username, self.password])
                save = True
        return save


if __name__ == "__main__":
    u = Utilisateur("AYMERIC1", "aymeric1")
    print(u.events.get_all_events())
    u.events.add_event("5/24/20", "Event4", 5)
    u.events.add_event("5/25/20", "Event5", 5)
    print(u.events.get_all_events())
    u.events.remove_event("5/24/20", "Event4")
