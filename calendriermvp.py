import calendar
import csv

# création de la classe event
class Event :
   def __init__(self, date, event, createur):
    self.date = date
    self.event = event
    self.createur = createur

#Choix de l'action ( ajout, voir et supprimer event )
choixAction=0
it_choixAction = False
while it_choixAction == False or choixAction<1 or choixAction>4 : 
   try : 
      choixAction = int(input("que voulez vous faire 1 entrer un event 2 voir event a une date 3 supprimer un event 4 voir tout les events ?"))
      it_choixAction = True
   except ValueError : 
      it_choixAction = False



# fonction de traitement de réception de la date 
def choix_date(valeur) :


   def choix_annee() :
      it_year=False
      while it_year == False :
         try:
            year = int(input("Choisissez l'année "))

            it_year = True
         except ValueError:
            it_year = False
      resultat = str(year)
      return resultat
      
   def choix_mois() :
      it_year=False
      it_month=False
      month=0
      while it_year == False :
         try:
            year = int(input("Choisissez l'année "))

            it_year = True
         except ValueError:
            it_year = False

     
      while it_month == False :
         try:
            while month<=0 or month>12 : 
               month = int(input("Choisissez le mois "))
         
            it_month = True
         except ValueError:
            it_month = False
      resultat = str(year)+"/"+str(month)
      return resultat

   def choix_jours () :
      it_year=False
      it_month=False
      month=0
      it_days=False
      days=0
      while it_year == False :
         try:
            year = int(input("Choisissez l'année "))

            it_year = True
         except ValueError:
            it_year = False
            
      
      while it_month == False :
         try:
            while month<=0 or month>12 : 
               month = int(input("Choisissez le mois "))
         
            it_month = True
         except ValueError:
            it_month = False

      while it_days == False :
         try:
            if month==1 or month==3 or month ==5 or month==7 or month ==8 or month==10 or month ==12 :
               while days<=0 or days>=31 : 
                  days = int(input("Choisissez le jour "))
            
               it_days = True
            if month==4 or month==6 or month ==9 or month==11 :
               while days<=0 or days>=30 : 
                  days = int(input("Choisissez le jour "))
            
               it_days = True
            else :
               while days<=0 or days>29 : 
                  days = int(input("Choisissez le jour "))
            
               it_days = True
         except ValueError:
               it_days = False

      resultat = str(year)+"/"+str(month)+"/"+str(days)
      return resultat
            
   if valeur == 'a' : 
      return choix_annee()
   if valeur == 'm' : 
      
      return choix_mois()
   else :
     
      return choix_jours()




# recherche et affichage de l'event présent à la date demandée
def lecture_event(date) : 
   presenceevent=0
   f= open (r"listing.csv")
   myReader = csv.reader(f)
   for row in myReader:
      if date in row[0]:
         print(row[0]+'   '+ row[1])
         presenceevent=presenceevent+1

   if presenceevent == 0 :
      print("vous n'avez aucuns event prévu le "+date)



# ajout d'un event à la date demandé

def ajout_event(date,event) :
   with open('listing.csv','a',newline='', encoding='utf-8') as fichiercsv:
       writer=csv.writer(fichiercsv)
       writer.writerow([date,event]) 
       fichiercsv.close()
       print("Votre event a bien été enregistré !")




# suppression de l'event présent à la date demandée.
def suppression_event(date):
   with open('listing.csv', 'rb') as inp, open('first_edit.csv', 'wb') as out:
    writer = csv.writer(out)
    for row in csv.reader(inp):
        if row[1] != date:
            writer.writerow(row)


# traitement de l'input de lutilisateur afin de savoir ce qu'il doit faire.
if choixAction == 1 :
   date=choix_date(3)
   event=input('quel est l event que vous voulez enregistrer')
   ajout_event(date,event)


if choixAction == 2 :
   angleinspection=""
   while angleinspection != 'a' and angleinspection!='m' and angleinspection!='j' :
      angleinspection=input("voulez vous chercher une année (a), un mois(m), un jour(j) ?")
   date=choix_date(angleinspection)
   lecture_event(date)

if choixAction == 3 :
   date=choix_date(3)
   suppression_event(date)

if choixAction==4 :
      f= open (r"listing.csv")
      myReader = csv.reader(f)
      for row in myReader:
         print(row[0]+'   '+ row[1])


#Les semaines du calendrier commenceront le lundi
calendar.setfirstweekday(calendar.MONDAY)

#Affiche un mois sélectionné de l'année sélectionné
#1 = janvier


#Affiche tous les mois de l'année sélectionné 
#mycal = calendar.calendar(year)
