%matplotlib inline
# Jean-Michel Torres 2018-10-16  TSP naïf (pas optimisé)
# lexicographical enumeration from Michal Forišek in :
# https://www.quora.com/How-would-you-explain-an-algorithm-that-generates-permutations-using-lexicographic-ordering              #
from random import randint
from math import factorial, sqrt
import matplotlib.pyplot as plt

def makeCities(total_cities, w, h):
    '''construction d'une liste de villes (définies par leur coordonnées tirées au sort)
    entrée : nombre de villes, dimensions w et h du terrain contenant les villes
    sortie : une liste de villes définies par leur coordonnées'''
    cities = []
    for i in range(total_cities):
        cities.append((randint(0,w),randint(0,h)))
    return cities

def makeOrder(total_cities):
    ''' création de la première permutation dans l'ordre lexocigraphiqu (0,1,2, ... , total_cities - 1)'''
    initial_order = []
    for i in range(total_cities):
        initial_order.append(i)
    return initial_order

def nextOrder(permutation):
    '''calcule la prochaine permutation dans l'ordre lexicographique, par exemple 23781 renvoie 23871
    en entrée une liste de nombres uniques, en sortie une liste dans l'ordre lexicographique qui suit. '''
    largestX = -1
    for x in range(len(permutation)-1):
        if (permutation[x] < permutation[x + 1]):
            largestX = x
    if largestX == -1: # on a terminé
        print("done")
        return 0
    largestY = -1
    for y in range(len(permutation)):
        if (permutation[largestX] < permutation[y]):
            largestY = y
    permutation[largestX],permutation[largestY] = permutation[largestY],permutation[largestX]
    endList = permutation[largestX + 1:]
    endList.sort()
    startList = permutation[:largestX + 1]
    return startList+ endList

def CalcDistance(permut,cities):
    '''calcul de la longueur du chemin entre les villes pour une permutation données'''
    itinerary_length = 0.0
    for j in range(total_cities - 1):
        #itinerary_length += distance.euclidean(cities[permut[j]],cities[permut[j + 1]])
        itinerary_length += sqrt((cities[permut[j]][0] - cities[permut[j+1]][0])**2
                             + (cities[permut[j]][1] - cities[permut[j+1]][1])**2)
    return itinerary_length

# SETUP ***************************************** nombre de ville et taille du terrain
total_cities = 9   # 8 ou 9 sont acceptables
width = 500 ; height = 300 ;iteration = 0 ; d = 0.0
# fabrication de la liste des villes
cities = makeCities(total_cities,width,height)
print("coordonnées des villes:", cities)

order = makeOrder(total_cities)
bestOrder = order
best = CalcDistance(order,cities)

print("début, il y aura ", factorial(total_cities) , "itérations")
for i in range(factorial(total_cities) - 1):
    iteration += 1
    order = nextOrder(order)
    d = CalcDistance(order,cities)
    if d < best:
        bestOrder = order.copy()
        best = d
        print(f"nouveau plus court chemin: {d:.1f} à l'itération: {iteration} (de {factorial(total_cities)})")
print(f"Terminé : {iteration }. meilleure {bestOrder}, longueur: {best:.1f}")

itinerary = []
for k in range(len(cities)):
    itinerary.append(cities[bestOrder[k]])

print(itinerary)
fig, ax = plt.subplots()
(x, y) = zip(*itinerary)
ax.plot(x, y, marker='o')
ax.set_xlim((0, width))
ax.set_ylim((0, height))
plt.show()
