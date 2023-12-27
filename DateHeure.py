from datetime import datetime

# Demander à l'utilisateur d'entrer la date 
chn_date =input("Entrez votre date d'anniversaire (ex : mois-jours-annee): ")

# convertir la date actuelle 
now_time = datetime.now().strftime("%d-%m-%Y")

# convertir la date actuelle en format datetime 
heure = datetime.strptime(now_time,"%d-%m-%Y")
 
# convertir la date d'anniversaire 
dateAnniversaire = datetime.strptime(chn_date,"%d-%m-%Y")

joursRestants =(dateAnniversaire - heure).days

print(f"{joursRestants} restant avant le : {dateAnniversaire.strftime("%d-%m-%Y")} ")

# print(heure)