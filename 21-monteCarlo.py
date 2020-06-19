### 2.1 estimation de 𝜋 avec la méthode de Monte-Carlo.
######################################################################################################
# ici nous allons utiliser le générateur de nombres alétatoires de python, dans la bibliotheque random
# la fonction random() nous donne un nombre compris entre 0 et 1 à chaque fois qu'on l'appelle.
# pour mesurer le temps d'exécution, nous avons besoin de la bibliotèque time
import time
from random import random

# on demande à l'utilisateur d'indiquer le nombre de points à tirer au sort.
nombre_de_points = int(input("combien de points voulez-vous tirer au sort ?:") )

# on utilise une variable qui va contenir le nombre de points à l'intérieur du quart de cercle
points_dedans = 0

# enregistrons l'instant du début de l'execution
debut = time.time()

# on utilise une boucle "for" pour tirer au sort le nombre de points demandés par l'utilisateur
for i in range(nombre_de_points):
    # appelons x et y les coordonnées du point que l'on tire au sort
    x = random()
    y = random()
    # si la somme des carrés des coordonnées du point est inférieure à 1 alors le point est à l'intérieur
    # du cercle. Bien sûr ici nous utilisons la formule du cercle.
    if x**2 + y**2 < 1:
        points_dedans += 1

# enregistrons l'instant de fin de l'exécution, on peut alors calculer la durée:
fin = time.time()
duree = fin - debut

# c'est terminé, points_dedans contient le nombre de points à l'intérieur du quart de cercle.
# pour un cerlce de rayon 1 la surface du quart de cercle vaut 𝜋/4 le carré de coté 1 a une surface égale à 1
# il suffit de multiplier le rapport des points_dedans par nombre_de_points par 4 pour obtenir une valeur de 𝜋 :

# enfin, affichons les résultats:
print(f"temps d'éxecution total : {duree:.1f} secondes")
print(f"estimation de 𝜋 = {4 * points_dedans / nombre_de_points}")
