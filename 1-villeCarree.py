### 1 taille de la ville carrée des Neufs Chapitres avec la méthode de Al-Khuwârizmî
####################################################################################
# comme nous aurons à calculer une racine carrée, il nous faut importer cette
# fonction depuis la bibliothèque des fonctions mathématiques de Python.
# La bibliothèqe s'appelle math, et la fonction est sqrt()
from math import sqrt
####################################################################################
# affectons les valeurs au variables nombre et racinesen Python la création et
# l'affectation d'une valeur à une variable est aussi simple que cela:
nombre = 2 * 1775 * 20
racines = 20 + 14
####################################################################################
# Nous appliquons maintenant la "recette" de Al-Khuwârizmî, en utilisant au fur et
# à mesure dez variables (A, B, C , D, E) pour enregistrer chaque résultat de calcul
# et s'en servir à l'étape suivante:
####################################################################################
# Prends la moitié des racines
A = racines / 2
# Multiplie ce résultat par lui-même
B = A * A
# Ajoute le résultat au nombre
C = B + nombre
# Prends la racine de ce résultat
D = sqrt(C)
# Soustrais-en la moitié des racines
E = D - ( racines / 2 )

# Nous avons terminé, affichons le résultat :
print(f"Chaque côté de la ville mesure {E} bùs ")
