###  3.1 tri à bulle
####################################################################################
# ici nous avons besoin de générer une liste de nombre aléatoire pour effectuer le tri
import random

def swap(liste, indice1, indice2):
    """ on définit une fonction à laquelle on fournit une liste et deux indices et cette fonction
        échange les valeurs des positions positions indice1 et indice2 dans la liste"""
    # on utilise une variable temporaire
    # on pourrait éviter en utilisant :
    #liste_a_trier[indice1],liste_a_trier[indice2] = liste_a_trier[indice2],liste_a_trier[indice1] )
    # normalement c'est plus lisible comme ceci :
    temporaire = liste_a_trier[indice1]
    liste_a_trier[indice1] = liste_a_trier[indice2]
    liste_a_trier[indice2] = temporaire

taille_de_la_liste = int(input("taille de la liste à trier: " ))
# define an array of n random numbers
liste_a_trier  = [int(random.random()*1000 + 0.5) for i in range(taille_de_la_liste)]
print(liste_a_trier)

# on va parcourir la liste à n reprises de manière à être certain de l'avoir triée même dans
# le cas le plus défavorable où l'élément le plus petit se trouvait à la fin (en exercice vous pouvez
# améliorer l'algorithme en l'arretant dès qu'il n'a plus effectué de changment dans la liste)
for i in range(taille_de_la_liste):
    #pour chaque élément dans la liste, on le compare à son voisin et on l'échange si besoin
    for j in range(taille_de_la_liste-1):
        if liste_a_trier[j+1] < liste_a_trier[j]:
            swap(liste_a_trier,j+1,j)

# on peut l'afficher (elle s'appelle toujours liste_a_trier, mais c'est fait, elle est triée)
print(liste_a_trier)
