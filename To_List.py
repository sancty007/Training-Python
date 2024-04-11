# Déclaration d'une liste vide pour stocker les tâches
taches = []

## Fonction pour ajouter une tâche à la liste
def ajouter_tache():
    valide = True
    while valide:
        ajouterListe = input("Ajouter une tache à la liste : ")

        if(len(ajouterListe)>0):
            taches.append(ajouterListe)

            print("Voulez-vous continuer à ajouter des éléments ?")

            reponse = input("oui|OUI|O ou NON|non|N : ").lower()

            if reponse == "non" or reponse == "n":
                valide = False
            elif reponse == "oui" or reponse == "O":
                continue
            else:
                print("Réponse invalide ")

    Affiche_menu()

# Fonction pour afficher les tâches
def afficher_taches():
    if len(taches) == 0:
        print("La liste est vide ...")
    else:
        print("La liste des taches...")
        for index ,tache in enumerate(taches, start=1):
            print(f'{index}. {tache}')
    print()# Ajout d'une ligne vide pour séparer la liste des tâches du menu
    Affiche_menu()

# Fonction pour marquer une tâche comme terminée
def marquer_terminee():
    valide = True
    inter = [i for i in range(len(taches))]
    while valide:
        try:
            numTache = int(input("Entrez le numéro de la tâche à supprimer : "))
            if numTache in inter:
                del taches[numTache]
                valide = False
                print("Tâche Terminée... ")
            elif len(taches) == 0:
                print("La liste est vide ")
                break
            else:
                print("Problème inconnu, contactez le développeur") 
        except:
            print("Index invalide : ce n'est pas un nombre ")
    Affiche_menu()

# Liste des options du menu
menu_liste = ["Ajouter une tache ", "Afficher les taches", 
              "Marquer une tache comme terminée", "Modifier une tache","Quitter"]

# Fonction pour afficher le menu
def Affiche_menu():
    print("Menu:")
    for i, k in enumerate(menu_liste):
        print(f"{i}: {k}")
    print()  # Ajoute une ligne vide pour améliorer la lisibilité
    Faire_choix()

## Fonction pour modifier une tache 
def Modifier_tach():
    valide = True
    inter = [i for i in range(len(taches))]
    while valide:
        try:
            numTache = int(input("Entrez le numéro de la tâche à modifier : "))
            if numTache not in inter:
                print("Problème inconnu, contactez le développeur")
            else:
                taches[numTache] = input("Entrez la nouvelle tâche : ")
                valide = False
        except:
            print("Index invalide : ce n'est pas un nombre ")
    Affiche_menu()

# Liste des fonctions correspondant aux options du menu
liste_Fonction = [ajouter_tache, afficher_taches, marquer_terminee,Modifier_tach, exit]


# Fonction pour que l'utilisateur fasse un choix
def Faire_choix():
    while True:
        try:
            choix_utilisateur = int(input("Entrez votre choix :"))
            break
        except Exception as e:
            print("Erreur de type : Entrez un chiffre valide ")
    valide = True 

    while valide:
        for index in range(len(liste_Fonction)):
            if choix_utilisateur == index:
                liste_Fonction[index]()
                valide = False  # Sortir de la boucle une fois que l'option est exécutée
            else:
                continue



# Affichage initial du menu
Affiche_menu()
