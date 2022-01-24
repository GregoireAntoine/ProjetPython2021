import calendar

year = int(input("Entrer l'année : "))
#month = int(input("Entrer le mois : "))

#Les semaines du calendrier commenceront le lundi
calendar.setfirstweekday(calendar.MONDAY)

#Affiche un mois sélectionné de l'année sélectionné
#1 = janvier
# mycal = calendar.month(year, month)

#Affiche tous les mois de l'année sélectionné 
mycal = calendar.calendar(year)

print(mycal)
