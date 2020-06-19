### 2.3 estimation de 𝜋 avec la méthode de François Viète
################################################################################
# comme déjà vu plus haut, on a besoin d'importer la fonction racine carrée.
from math import sqrt
nombre_de_termes = int(input("entrez le nombre de termes à calculer : "))
# initialisation du résultat avec le tout premier terme de la formule : 2
valeur_de_pi  = 2
# la variable denominateur va nous servir à faire le calcul d'un terme à l'autre
denominateur = sqrt(2)
for i in range(nombre_de_termes):
    valeur_de_pi = valeur_de_pi * 2 / denominateur
    # mise à jour de la valeur du dénominateur pour le prochain terme
    denominateur = sqrt(2 + denominateur)

print(valeur_de_pi)
