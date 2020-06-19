### 2.2 estimation de 𝜋 avec la méthode John Wallis.
######################################################################################################
def calcule_pi(k):
    """On définit une fontion calcule_pi qui prend un nombre entier en paramètre
       et qui calcule les n premiers termes de la formule de Wallis
    """
    # on initalise le produit de termes à la valeur 1
    prod = 1
    # pour n allant de 1 à k
    for n in range(1,k+1):
        # on multiplie le produit déjà obtenu par le terme d'ordre n de la formule de Wallis
        prod = prod*4*n*n/(4*n*n-1)
    # on n'oublie pas de multiplier par 2 à la fin
    return(2*prod)

# on demande à l'utilisateur le nombre de termes à calculer:
nombre_de_termes = int(input("entrez le nombre de termes à calculer : "))
# on appelle la fonction avec le nombre de termes en paramètre et on affiche le résultat
print(calcule_pi(nombre_de_termes))
          
