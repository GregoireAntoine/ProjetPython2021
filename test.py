import os
import unittest
import interfaceProjet
import os
import csv

class evenement :

        def __init__(self, date, event, createur,acteurs):
            """créer un evenement comprennat un sujet, un créateur, une date et des invités.

            PRE : seul les invites peuvent être nuls
            POST : Il va créer un evenement avec une date, unu sujet, un créateur et peut-être des invités

            """
            self.date = date
            self.event = event
            self.createur = createur
            self.acteurs=acteurs

        def enregistrement(self):
            """ une date, un sujet, un createur et des invités qui sont enregistrés dans un fichier csv

            PRE : Nnone
            POST : si enregistre les données recues dans un csv return true sinon return false
            """
            with open('listing.csv','a',newline='', encoding='utf-8') as fichiercsv:
                if len(self.date)>4 :
                    writer=csv.writer(fichiercsv)
                    writer.writerow([self.date,self.event,self.createur,self.acteurs]) 
                    fichiercsv.close()
                    print("Votre event a bien été enregistré !")
                    return True
                else : 
                    fichiercsv.close()
                    print("Evenement", "Veuillez choisir une date")
                    return False 
                
                
        def participants(self) : 
            """Verifie les events d'une personne

            PRE : None
            POST : si il n'y a pas d'évènement return false sinon true
            """
            partici=[]
            verif=0
            crea=""
            f= open (r"listing.csv")
            myReader = csv.reader(f)
            print("feqgrehrj")
            for row in myReader:
                if row[1]== self.event and row[0]==self.date :
                    crea=row[2]
                    partici.append([row[3]])
                    verif=1
            if verif!=1 :
                print("Votre evènement", "Créateur : "+crea +"\n"+"participants : aucuns")
                return False
            else :  
                print("Votre evènement", "Créateur : "+crea +"\n"+"participants : "+partici[0][0])
                return True 


        def veriflsite():
            """Verifie qu'une liste existe

            PRE : None
            POST : si elle existe pas return false sinon true
            """
            f= open (r"listing.csv")
            myReader = csv.reader(f)
            if len(f)==0 : 
                return False 
            else : return True

        def suppresion(self) :
            """Supprime un evenement

            PRE : recois une date, un sujet, un createur 
            POST : si il est possible pour la personne de supprimer cet event return True sinon return False
            """
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
                print("Votre evènement", "il n'y a pas d'évènement à suprimmer ")
                return False
            else :
                print("Votre evènement", "évènement bien supprimé ")
                return True


class projettest(unittest.TestCase) :
    def __init__(self, methodName):
        super().__init__(methodName)
        self.event1=evenement("21/05/2020","test","Gregoire","Aymeric123")
        self.event2=evenement("21","Annif zebi corse","aaaaaaaa","")
        self.event3 =evenement("21/07/2020","afgesfd","Aylercirefzgrehtg","Aymeric123")
        self.event4 =evenement("","afgesfd","Aylercirefzgrehtg","Aymeric123")
        self.event5=evenement("21/07/2022","afgefeswgrdtxhsfd","Aylercefzgrethryjirefzgrehtg","fdfsgwhdfxc123")
        self.event6=evenement("21/07/2","afgesfd","Aylercirefzgrehtg","Aymeric123")
        
    def test_participants(self) : 
        self.assertTrue(self.event3.participants())
        self.assertFalse(self.event2.participants())
        self.assertFalse(self.event6.participants())
        

    def test_suppression(self) : 
        self.assertTrue(self.event5.suppresion())
        self.assertFalse(self.event4.suppresion()) 

    def test_enregistrement (self) :
        self.assertTrue(self.event3.enregistrement())
        self.assertFalse(self.event2.enregistrement())
        self.assertTrue(self.event1.enregistrement())
        self.assertFalse(self.event4.enregistrement())
 
 

if __name__ == '__main__':
    unittest.main()