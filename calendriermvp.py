import calendar
import csv
it_month=False
it_year=False


choix = input("que voulez vous faire 1 entrer un event 2 voir event a une date ?")

# input et vérification de l'input.

def choix_date() :
   while it_year == False :
      try:
         year = int(input("Choisissez l'année "))

         it_year = True
      except ValueError:
         it_year = False

   while it_month == False :
      try:
         month = int(input("Choisissez le mois "))
         while month<=0 or month>12 :
            month = int(input("Choisissez le mois "))
            it_month = True
      except ValueError:
         it_month = False
   date=str(year)+' '+str(month)
   return date


def lecture_event(date) : 
   f= open (r"listing.csv")
   myReader = csv.reader(f)
   for row in myReader:
      print(row[0]+'   '+ row[1])

def ajout_event(date,event) :
   with open('listing.csv','a',newline='', encoding='utf-8') as fichiercsv:
       writer=csv.writer(fichiercsv)
       writer.writerow([date,event]) 
       fichiercsv.close()
       print("Vos données ont bien été enregistrées !")



if choix == 1 :
   date=choix_date()
   event=input('quel est l event que vous voulez enregistrer')
   ajout_event(date,event)


if choix == 2 :
   date=choix_date()
   lecture_event(date)




#Les semaines du calendrier commenceront le lundi
calendar.setfirstweekday(calendar.MONDAY)

#Affiche un mois sélectionné de l'année sélectionné
#1 = janvier


#Affiche tous les mois de l'année sélectionné 
#mycal = calendar.calendar(year)
