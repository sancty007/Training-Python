from datetime import datetime

now_time = datetime.now().strftime("%d-%m-%Y")

heure = datetime.strptime(now_time,"%d-%m-%Y")

chn_date ="01-01-2024"
dateAnniversaire = datetime.strptime(chn_date,"%d-%m-%Y")

joursRestants =(dateAnniversaire - heure).days


print(f"{joursRestants} restant avant le : {dateAnniversaire.strftime("%d-%m-%Y")} ")

# print(heure)