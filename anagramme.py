import itertools

# Entrer une phrase ou un mot 

#word = input("Please enter anagramme word : ")

listAnagramme = ["art","are","bat","ant","nap","top","dog","rca"]

word = "arc"
listWord2 = ["".join(i) for i in itertools.permutations(word)]

print(listWord2)
print(listAnagramme)

def anagramme_verify():
    i = 0
    while (i < len(listWord2)) :
        if listWord2[i] in listAnagramme :
            return True
        i+=1
    else:
            return False
   

if (anagramme_verify()) : 
    print("Le mot est anagramme !")
else :
    print("Le mot n'est pas un anagramme !")
        



""" print(listWord2)
print(len(listWord2)) """