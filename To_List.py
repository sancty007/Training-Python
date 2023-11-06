# creation  de la list 

taches =[] 
   
def ajouter_tache():
    valide = True
    reponse =""
    while valide == True:
        ajouterListe = input("Ajouter une tache à la liste : ")
        taches.append(ajouterListe)
        print("voulez vous continuer à ajouter des element?")
        reponse=input("oui|Oui ou Non|non : ").lower()
        if reponse =="non" :
            valide = False
        elif reponse =="oui":
            continue     
        else :
            print("Reponse invalide ")  
    Affiche_menu()
            
def afficher_taches():
    if len(taches) == 0 :
        print("La liste est vide ...")
    else :
        print(taches)
    Affiche_menu()     

def supprimer_tache():
    pass

def marquer_terminee():
    valide = True
    inter = [i for i in range (len(taches))]
    while valide == True :
        try :
            numTache=int(input("Entrez le numero de la tâche à supprimer : "))
            """ if numTache not in inter:
                print("Probleme d'index ...")
                #continue """
            if numTache in inter:
                del taches[numTache]
                valide = False
                print("Tache Terminee... ")
            elif  len(taches)== 0:
               print("la liste est vide ")
               break
            else :
                print("probleme inconnu contactez le dev") 
        except :
            print("index invalide  : n'est pas un nombre ")
    Affiche_menu()


        
menu_liste =["Ajouter une tache ","Afficher les taches", 
             "Marquer une tache comme terminee" , "Quitter"]
def Affiche_menu():
    for i,k in enumerate(menu_liste) :
        print(f"{i}: {k} \n")
    Faire_choix() 

liste_Fonction=[ajouter_tache,afficher_taches,marquer_terminee,exit]

def Faire_choix():
    while True :
        try :
            choix_utilisateur =int(input("Entrez votre choix :"))
            break
        except Exception as e :
            print("Erreur de type : Entrez un chiffre valide " )
    valide =True 

    while valide == True:
        for index in range(0,len(liste_Fonction)):
            if choix_utilisateur == index :
                liste_Fonction[index]()
            else :
                continue 
        


# Affiche Liste 


Affiche_menu()

