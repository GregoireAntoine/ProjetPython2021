import os
import csv


class Evenements:
    FILENAME_EVENTS = "listing.csv"

    def __init__(self, username):
        self.username = username

    def event_already_exists(self, date, name):
        """Si un évènement existe

        PRE : Reçoit une date, un nom, un username 
        POST : Si les arguments reçus correspondent à un évènement qui existe déjà renvoi True
        """
        ret = False
        if os.path.exists(self.FILENAME_EVENTS):
            with open(self.FILENAME_EVENTS, 'r') as csvfile:
                csv_reader = csv.reader(csvfile)
                for row in csv_reader:
                    if len(row):
                        if row[0] == date and row[1] == name and row[2] == self.username:
                            ret = True
        return ret

    def add_event(self, date, name, acteurs):
        """Ajout d'évènement

        PRE : Reçoit une date, un nom, un username 
        POST : Si les arguments reçus ne correspondent à aucun évènement qui existe déjà, renvoi True et le créé l'évènement
        """
        ret = False
        if os.path.exists(self.FILENAME_EVENTS):
            with open(self.FILENAME_EVENTS, "a", newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow([date, name, self.username, acteurs])
                ret = True
        else:
            with open(self.FILENAME_EVENTS, "w", newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow([date, name, self.username, acteurs])
                ret = True
        return ret

    def get_event(self, date, name):
        """Récuperer un évènement

        PRE : Reçoit une date, un nom, un username 
        POST : Si les arguments reçus correspondent à un évènement qui existe déjà renvoi True
        """
        e = None
        if os.path.exists(self.FILENAME_EVENTS):
            with open(self.FILENAME_EVENTS, 'r') as csvfile:
                csv_reader = csv.reader(csvfile)
                for row in csv_reader:
                    if len(row):
                        if date == row[0] and name == row[1]:
                            e = (row[0], row[1], row[2], row[3])  # tuple
        return e

    def get_events_date(self, date):
        l = []
        if os.path.exists(self.FILENAME_EVENTS):
            with open(self.FILENAME_EVENTS, 'r') as csvfile:
                csv_reader = csv.reader(csvfile)
                for row in csv_reader:
                    if len(row):
                        if date == row[0]:
                            l.append((row[0], row[1], row[2], row[3]))  # tuple (comme une liste mais on ne peut pas modifier)
        return l

    def get_all_events(self):
        l = []
        if os.path.exists(self.FILENAME_EVENTS):
            with open(self.FILENAME_EVENTS, 'r') as csvfile:
                csv_reader = csv.reader(csvfile)
                for row in csv_reader:
                    if len(row):
                        l.append((row[0], row[1], row[2], row[3]))  # tuple
        return l
    
    def remove_event(self, date, name):
        lines = []
        n = 0
        if os.path.exists(self.FILENAME_EVENTS):
            with open(self.FILENAME_EVENTS, "r") as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if len(row):
                        if row[0] != date or row[1] != name or row[2] != self.username:
                            lines.append(row)
                        else:
                            n += 1
            with open(self.FILENAME_EVENTS, "w", newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(lines)
        return n > 0


if __name__ == "__main__":
    e = Evenements("AYMERIC1")
    e.add_event("5/22/20", "Event1", 5)
    e.add_event("5/23/20", "Event2", 5)
    print(e.get_all_events())
    e.remove_event("5/23/20", "Event2")
    print("done")
