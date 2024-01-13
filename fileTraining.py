def entrerNomFichier():
    return suppressionCaractereSpeciaux(input("Entrez le nom du fichier à stocker : "))

def entrerContenue():
    return input("Entrez le contenu du fichier : ")

def suppressionCaractereSpeciaux(phrase):
    # Retire les ponctuations et caractères spéciaux
    return "".join(e for e in phrase if e.isalnum())

def ecritDansFichier(nom_fichier, contenu):
    with open(nom_fichier, 'w', encoding='utf-8') as fichier:
        fichier.write(contenu)

def messageValidation(nom_fichier, contenu):
    try:
        ecritDansFichier(nom_fichier, contenu)
        print("Opération réussie.")
    except Exception as e:
        print(f"L'opération a échoué. Erreur : {e}")

# Obtenir les valeurs avant d'appeler les fonctions
nom_fichier = entrerNomFichier()
contenu = entrerContenue()

ecritDansFichier(nom_fichier, contenu)
messageValidation(nom_fichier, contenu)
