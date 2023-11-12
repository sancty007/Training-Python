import string

def monStyle(fonction) :
    def sous_fonction():
        print("-----------------------------------------")
        fonction()
        print("-----------------------------------------")
    return sous_fonction




def ispalindrome (phrase :str):

    # Retire les ponctuations et caractère speciaux , et met chaque element en miniscule avec lower()
    noponctuattion = "".join(e.lower() for e in phrase if e.isalnum())

    inversePhrase= noponctuattion[::-1] 

    # condition de verification si l'inverse est egale à la phrase originale 
    if inversePhrase == noponctuattion : 
        return True


var = "Eva, Can I See Bees In A Cave?"


@monStyle
def Message() :
    if ispalindrome(var) is True:
        print("La phrase est un palindrome")
    else :
        print("La phrase n'est pas  un palindrome")

Message()      
    
