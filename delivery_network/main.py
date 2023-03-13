from graph import UnionFind
from graph import Graph, graph_from_file, temps_calcul_kruskal, power_min_kruskal, represente

##test de la question 7##

G="/home/onyxia/work/Ensae-prog23/input/network.00.in"
represente(G, 1, 2)
represente(G, 8, 6)

G1="/home/onyxia/work/Ensae-prog23/input/network.01.in"
represente(G1, 1, 3) 
represente(G1, 7, 3) #renvoie bien none car 7 et 3 ne sont pas des composantes connectées 

# On test la fonction kruskal ? 
g1 = graph_from_file("/home/onyxia/work/Ensae-prog23/input/network.00.in")
g2 = graph_from_file("/home/onyxia/work/Ensae-prog23/input/network.01.in")
g3 = graph_from_file("/home/onyxia/work/Ensae-prog23/input/network.02.in")
g4 = graph_from_file("/home/onyxia/work/Ensae-prog23/input/network.03.in")
print("Voici g1.kruskal", g1.kruskal())
print("Voici g2.kruskal", g2.kruskal())
print("Voici g3.kruskal", g3.kruskal())
print("Voici g4.kruskal", g4.kruskal())


##Question 1 du tp2##
#print(temps_calcul_naif("/home/onyxia/work/Ensae-prog23/input/network.1.in", "/home/onyxia/work/Ensae-prog23/input/routes.1.in"))
#print(temps_calcul_naif("/home/onyxia/work/Ensae-prog23/input/network.2.in", "/home/onyxia/work/Ensae-prog23/input/routes.2.in"))
#en faisant le test plusieurs fois, sur route.1.in et le graphe 1, on observe que le temps est très court (0.02 secondes)
#Si on prend la route 2 et le graphe 2, on voit que le temps nécessaire est entre 30h et 50h. C'est beaucoup trop long!!


##test question4 du tp2
#print(test_kruskal())



##question 5 du tp2##
"""print(temps_calcul_kruskal("input/network.1.in", "input/routes.1.in"))
print(temps_calcul_kruskal("input/network.2.in", "input/routes.2.in"))
print(temps_calcul_kruskal("input/network.3.in", "input/routes.3.in"))
print(temps_calcul_kruskal("input/network.4.in", "input/routes.4.in"))
print(temps_calcul_kruskal("input/network.5.in", "input/routes.5.in"))
print(temps_calcul_kruskal("input/network.6.in", "input/routes.6.in"))
print(temps_calcul_kruskal("input/network.7.in", "input/routes.7.in"))
print(temps_calcul_kruskal("input/network.8.in", "input/routes.8.in"))
print(temps_calcul_kruskal("input/network.9.in", "input/routes.9.in"))"""

#on trouve des temps beaucoup plus courts. Par exemple pour le premier, on trouve 0.002 sec
#pour le second, on trouve environ 3h
#pour le troisième, on trouve environ 20h
#pour le 5eme, 7h
#pour le dernier, on trouve environ 30h
#on trouve donc des temps bien plus courts!!

#print(calcul_trajets_total("input/network.2.in", "input/routes.2.in"))