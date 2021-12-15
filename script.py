import csv


def dernierevent () : 
   presenceevent=0
   compteur=0
   tableau=[]
   f= open (r"listing.csv")
   myReader = csv.reader(f)
   for row in myReader:
      if "GREG" in row[2] :
         tableau.append(row[0]+ row[1])
         compteur=compteur+1
         presenceevent=presenceevent+1

   
   return tableau[len(tableau)-1]


def enregistrement_event(date,event) :
   with open('listing.csv','a',newline='', encoding='utf-8') as fichiercsv:
       writer=csv.writer(fichiercsv)
       writer.writerow([date,event,"GREG"]) 
       fichiercsv.close()
       print("Votre event a bien été enregistré !")


