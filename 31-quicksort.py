### 3.2 quicksort
####################################################################################
# importations pour fabriquer les valeurs du tableau à trier et mesurer la durée d'exécution
import random, time

def quicksort(arr, start, end):
    if start >= end:
        # c'est terminé (liste de taille 0)
        return
    # on calcule l'index pivot avec la fonction "partition"
    index = partition(arr, start, end)
    # et on appelle cette fonction pour les deux sous-tableaux, à gauche et à droite de l'index pivot:
    quicksort(arr,start,index - 1)
    quicksort(arr,index + 1, end)

def partition(arr,debut,fin):
    """cette fonction va parcourir la partie de la liste entre 2 positions (début et fin)
       la valeur de l'élément de fin est la "valeur pivot", la valeur pivot est fixée
       pour chaque execution de la fonction partition.
       on parcourt la partie de liste entre début et fin. On se dote d'un index qui commence
       par pointer sur le premier élément de la partie de liste traitée.
       Si la valeur de l'élément courant de l'itaration est inférieure à la valeur pivot,
       alors on swappe cet élément courant avec l'élément pointé par l'index, et on incrémente l'index.
       A la fin de l'itération, tous les éléments dont la valeur est inférieure à celle de la valeur
       pivot se retrouvent placés à une position inférieure à l'index. Il reste à placer l'élément
       de la valeur pivot à cet endroit. On renvoie l'index qui permet ensuite d'effectuer la même
       opérations pour les 2 sous listes (celle à gauche de l'index et celle à droite de l'index)
    """
    # on commence par initialiser l'index pivot à gauche de la liste, car on va parcourir la liste du
    # début à la fin, une fois. A chaque fois qu'on a trouvé une valeur inférieure
    index = debut
    # on initialise la valeur du pivot arbitrairement à la valeur de l'élément de droite de la liste
    pivotvalue = arr[fin]
    # pour chacun des éléments de la liste, si leur valeur est inférieure à la valeur du pivot,
    # on le met à la position de l'index (qui a commencé par pointer le début de liste) et on
    #incrémente l'index.
    for i in range (debut,fin):
        if arr[i] < pivotvalue:
            arr[i], arr[index] = arr[index], arr[i]
            index +=1
    # pour finir on swappe l'élément qui contient la valeur pivot (celui de fin de liste)
    # pour le placer à la position de l'index et on retourne l'index
    arr[index], arr[fin] = arr[fin], arr[index]
    return index

taille = int(input("Entrez la taille de la liste à trier: "))
arr = [random.random() for i in range(taille)]
start_time = time.time()
quicksort(arr, 0, taille - 1)
duree = time.time() - start_time
print(f"Durée d'execution : {duree:.4f} seconde(s)")
print(arr) # pour se convaincre que ça a fonctionné, attention pour les grandes tailles de liste
