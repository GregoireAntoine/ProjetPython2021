import calendar
it_month=False
it_year=False
# input et vérification de l'input.
while it_year == False :
 try:
    year = int(input("Choisissez l'année "))

    it_year = True
 except ValueError:
    it_year = False

while it_month == False :
 try:
    month = int(input("Choisissez le mois "))

    it_month = True
 except ValueError:
    it_month = False



#Les semaines du calendrier commenceront le lundi
calendar.setfirstweekday(calendar.MONDAY)

#Affiche un mois sélectionné de l'année sélectionné
#1 = janvier
mycal = calendar.month(year, month)

#Affiche tous les mois de l'année sélectionné 
#mycal = calendar.calendar(year)

print(mycal)