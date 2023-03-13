#cette classe UnionFind nous sera utile dans le td2, pour la question 3
#elle sert à manipuler les composantes connexes efficacement et facilement
class UnionFind(object):
    '''classe UnionFind '''
    def __init__(self, n):
        assert n > 0, "n doit être strictement positif"
        self.n = n
        # cahque sommet est son propre parent au début
        for i in range(n) : 
            self.parent = [i]
    
    def find(self, i):
        '''On trouve le parent d'un élément et on remplace le chemin par le parent '''
        if self.parent[i] != i:
            # on remplace les éléments du chemin par leur parent
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
     
    def connectes(self, x, y):
        '''On vérifie si x et y sont connectés càd s'ils ont le même parent'''
        if self.find(x) == self.find(y):
            return True
        else:
            return False
    
    def union(self, x, y):
        '''On unit deux éléments en réunissant leurs parents'''
        xparent = self.find(x)
        yparent = self.find(y)
        if xparent != yparent:
            self.parent[yparent] = xparent

import time
import sys
sys.setrecursionlimit(200000)
class Graph:
    """
    A class representing graphs as adjacency lists and implementing various algorithms on the graphs. Graphs in the class are not oriented. 
    Attributes: 
    -----------
    nodes: NodeType
        A list of nodes. Nodes can be of any immutable type, e.g., integer, float, or string.
        We will usually use a list of integers 1, ..., n.
    graph: dict
        A dictionnary that contains the adjacency list of each node in the form
        graph[node] = [(neighbor1, p1, d1), (neighbor1, p1, d1), ...]
        where p1 is the minimal power on the edge (node, neighbor1) and d1 is the distance on the edge
    nb_nodes: int
        The number of nodes.
    nb_edges: int
        The number of edges. 
    """

    def __init__(self, nodes=[]):
        """
        Initializes the graph with a set of nodes, and no edges. 
        Parameters: 
        -----------
        nodes: list, optional
            A list of nodes. Default is empty.
        """
        self.nodes = nodes
        self.graph = dict([(n, []) for n in nodes])
        self.nb_nodes = len(nodes)
        self.nb_edges = 0
    

    def __str__(self):
        """Prints the graph as a list of neighbors for each node (one per line)"""
        if not self.graph:
            output = "The graph is empty"            
        else:
            output = f"The graph has {self.nb_nodes} nodes and {self.nb_edges} edges.\n"
            for source, destination in self.graph.items():
                output += f"{source}-->{destination}\n"
        return output
    
    def add_edge(self, node1, node2, power_min, dist=1):
        """
        Adds an edge to the graph. Graphs are not oriented, hence an edge is added to the adjacency list of both end nodes. 
        Parameters: 
        -----------
        node1: NodeType
            First end (node) of the edge
        node2: NodeType
            Second end (node) of the edge
        power_min: numeric (int or float)
            Minimum power on this edge
        dist: numeric (int or float), optional
            Distance between node1 and node2 on the edge. Default is 1.
        """
        if node1 not in self.graph:
            self.graph[node1] = []
            self.nb_nodes += 1
            self.nodes.append(node1)
        if node2 not in self.graph:
            self.graph[node2] = []
            self.nb_nodes += 1
            self.nodes.append(node2)

        self.graph[node1].append((node2, power_min, dist))
        self.graph[node2].append((node1, power_min, dist))
        self.nb_edges += 1
    
    

    def get_path_with_power(self, src, dest, power):
        #on fait un parcours en profondeur, on regarde si les étiquettes sont bien toutes plus petites que power
        #manque la com:plexité

        marquage = [False for i in range(self.nb_nodes)]
        pred=[-1 for i in range(self.nb_nodes) ]

        def dfs_rec(s) :
            marquage[s-1]=True
            for voisin in self.graph[s] :
                (i,j,k)=voisin #i : noeud voisin, j puissance minimal, k distance

                if not (marquage[i-1]) and j<=power :

                    marquage[i-1]=True
                    pred[i-1]=s
                    dfs_rec(i)

        dfs_rec(src)

        if marquage[dest-1]==False :
            return None
        chemin = [dest]

        p=dest

        while p != src :
            p=pred[p-1]
            chemin.append(p)

        n=len(chemin)

        for i in range(n//2) :
            chemin[i],chemin[n-1-i]=chemin[n-1-i], chemin[i]

        return chemin


    def connected_components(self):
        comp_connexe = []
        marquage = [False for i in range(0,self.nb_nodes)]

        def dfs_rec(s):
            comp = [s]
            marquage[s-1] = True

            for i in self.graph[s]:
                i = i[0]

                if marquage[i-1] == False:
                    marquage[i-1] = True
                    comp += dfs_rec(i)
            return comp           

        for noeud in self.nodes:

            if marquage[noeud-1] == False:
                comp_connexe.append(dfs_rec(noeud))

        return comp_connexe


    def connected_components_set(self):
        """
        The result should be a set of frozensets (one per component), 
        For instance, for network01.in: {frozenset({1, 2, 3}), frozenset({4, 5, 6, 7})}
        """
        return set(map(frozenset, self.connected_components()))
    
    #start = time.perf_counter()
    def min_power(self, src, dest):

        """
        Should return path, min_power. 
        """
        #il faut trouver une puissance qui marche
        #on teste avec des 2**n pour limiter la complexité
        #deja il faut voir si un chemin existe 
        #ou bien puissance infinie ou bien meme composante connexes

        power=float("inf")

        if self.get_path_with_power(src, dest, power) == None :

            return None #pas de chemin possible

        else :

            #il existe un chemin et une puissance minimale
            #on cherche alors une puissance et un entier n tel que 2**n marche, on sait alors que p min sera entre 2**n-1 et 2**n

            n=0

            while self.get_path_with_power(src, dest, 2**n) == None :
                n+=1

            #on fait la dico
            a=2**(n-1)
            b=2**n

            while b-a>1 :

                m=(a+b)//2
                if self.get_path_with_power(src, dest, m) == None :
                    a=m
                else :
                    b=m

        return (self.get_path_with_power(src, dest, b),b)
    
    #end = time.perf_counter()
    #temps_ecoule = (end - start)
    #print(temps_ecoule)

    def plus_court_chemin(self, src, dest, power) :
        #on fait une file de priorité
                f=queue.PriorityQueue()
                dist=[-1 for i in range(self.nb_nodes)]
                marquage = [False for i in range(self.nb_nodes)]
                pred=[-1 for i in range(self.nb_nodes)] 
                dist[src-1]=0
                marquage[src-1]=True  
                f.put(src, 0)
        
                while not f.empty() : 
                    u=f.get()
                    marquage[u-1]=True
                    for voisin in self.graph[u] :
                        (i,j,k)=voisin #i : noeud voisin, j puissance minimale, k distance
                        if not (marquage[i-1]) and j<=power and (dist[i-1]==-1 or dist[i-1]>d+k):
                            marquage[i-1]=True
                            pred[i-1]=u
                            dist[i-1]=dist[u-1]+k
                            f.put(i, dist[u-1]+k)
                    
            
                if marquage[dest-1]==False :
                    return None
                chemin = [dest]
                p=dest
                while p != src :
                    p=pred[p-1]
                    chemin.append(p)
                n=len(chemin)
                for i in range(n//2) :     

                    chemin[i],chemin[n-1-i]=chemin[n-1-i], chemin[i]
                return chemin

    

    # Fonction pour trouver l'arbre couvrant minimum
    def kruskal(self) :
        """Renvoie un arbre couvrant de poids minimal de self"""
        #on utilise la class unionfind qui se trouve au début de la page
        uf=UnionFind(self.nb_nodes) #créationd'une structure Union Find
        dico=self.graph             
        Gf=Graph([k for k in range(1,self.nb_nodes)]) #on crée notre nouveau graphe
        liste_arrete=[] #on va stocker toutes les listes d'arrêtes dans un tableau
        for i in range (1,self.nb_nodes) :
            for d in dico[i] : #on parcourt chaque liste associée au sommet i
                (a,b,c)=d #a=node2, b=power, c=dist
                if i< a : #on ajoute les arrêtes seulement une fois dans liste_arrete
                    liste_arrete.append((i,a,b))
        
        liste_arrete=sorted(liste_arrete, key=lambda x : x[2]) #on trie la liste des arrêtes en fonction de leur power
        for arrete in liste_arrete :
            (i,a,b)=arrete
            #On ne crée pas de cycles en rajoutant l'arrete (s1,s2) lorsque les deux sommets s1 et s2 ne sont pas dans la même composante connexe
            #si ils sont dans la même composante connexe alors en rajoutant l'arrête, on crée un cycle car alors deux chemins joignent ces sommets
            if not uf.connectes(i-1,a-1) : #si i et a ne sont pas dans les mêmes composantes connexes
                Gf.add_edge(i, a, b) #on rajoute l'arrête dans le nouveau graphe
                uf.union(i-1,a-1) # les deux sommets i et a sont maintenant dans la même composante connexe
        return Gf

def power_min_kruskal(g, src, dest) :
    """Renvoie  pour un trajet t=(src, dest) et g un arbre couvrant, la puissance minimale (et un chemin associé) d'un camion pouvant couvrir ce trajet"""
    # Prérequis : on suppose g est couvrant de poids minimal. 
    # Ainsi, si le chemin entre src et dest existe, il est unique
    #on fait un parcours comme on a déjà fait précedemment
    marquage = [False for i in range(g.nb_nodes)]
    pred=[-1 for i in range(g.nb_nodes)]
    def dfs_rec(s) :            
        marquage[s-1]=True
        for voisin in g.graph[s] :
            (i,j,k)=voisin #i : noeud voisin, j puissance minimale, k distance
            if not (marquage[i-1]) :
                marquage[i-1]=True
                pred[i-1]=(s,j) #on stocke des couples dans le tableau de prédecesseurs pour avoir accès à la puissance de l'arrête (s,i) plus simplement
                dfs_rec(i)
    dfs_rec(src)
    if marquage[dest-1]==False :
        return None
    chemin = [dest]
    #on va calculer la puissance minimale nécessaire.
    #Pour cela, on construit le chemin pour aller de src à dest et on regarde le power de chaque arrête
    #la puissance minimale vaut le max de ces puissances    
    p=dest
    power_min=0
    while p != src :
        (p, power)=pred[p-1] #on prend le couple
        chemin.append(p)        
        power_min=max(power_min, power) #on regarde si power > power_min, auquel cas il faut augmenter la puissance minimale pour passer
    n=len(chemin)
    for i in range(n//2) :            
        chemin[i],chemin[n-1-i]=chemin[n-1-i], chemin[i]
    return (chemin, power_min)

def temps_calcul_kruskal(G1, trajet, n=15) :
    """Renvoie le temps nécessaire pour calculer la puissance minimale sur l'ensemble des trajets en utilisant l'algorithme de Kruskal.
    Pramamètres :
    -G1 : type str, nom du fichier du graphe
    -trajet : type str, nom du fichier où on pioche les trajets
    -n : indique le nombre de trajets où l'on fait réellement le calcul"""
    #même principe que pour temps_calcul_naif sauf qu'on passe par l'arbre de Kruskal, pour les explications voir au-dessus
    g=graph_from_file(G1)
    G=g.kruskal() #on prend l'arbre de Kruskal

    trajets=open(trajet)
    line=trajets.readline().split()
    nb=int(line[0])
    moy=0
    i = 0
    trajets.close()
    while i < n :
        trajets=open(trajet)
        traj=random.randint(1,nb)
        for k in range(0, traj-1) :
            trajets.readline()        
        line=trajets.readline().split()                   
        (src, dest)=(int(line[0]), int(line[1]))        
        t0=time.perf_counter()
        power_min_kruskal(G,src, dest)
        t=time.perf_counter()-t0
        moy+=t
        i+=1
        trajets.close()  
   
    return((moy/n)*float(nb))

def graph_from_file(filename):
    """
        
        Reads a text file and returns the graph as an object of the Graph class.
        The file should have the following format: 

        The first line of the file is 'n m'

        The next m lines have 'node1 node2 power_min dist' or 'node1 node2 power_min' (if dist is missing, it will be set to 1 by default)

        The nodes (node1, node2) should be named 1..n

        All values are integers.
        Parameters: 
        filename: str

        The name of the file
        Outputs: 
        -----------
        G: Graph
        g: Graph
        An object of the class Graph with the graph from file_name.
        """
    f = open(filename)
    ligne = f.readline().split()
    nb_nodes = int(ligne[0])
    nb_edges = int(ligne[1])
    nodes = [i for i in range(1, nb_nodes+1)]
    G = Graph(nodes)
    for i in range(nb_edges):
        line = f.readline().split()
        if len(line) == 4:
            G.add_edge(int(line[0]), int(line[1]), int(line[2]), int(line[3]))
        else:
            G.add_edge(int(line[0]), int(line[1]), int(line[2]), 1)
    f.close()
    return G

import time
import math
import random
##tp2



import graphviz

def represente(G, src, dest, power=20) :
    """Résultat : Crée une image PNG qui est une représentation graphique du graphe de G, ainsi que du chemin associé trouvé"""
    graphe=graph_from_file(G) #on crée le graphe avec la class Graph associé à G
    g=graphviz.Graph(filename='G', format='png', directory="delivery_network", engine='dot') #on crée un graphe Graphviz
    chemin=graphe.get_path_with_power(src, dest, power ) #on trouve un chemin associé à la puissance power,
    #on aurait pu ne pas mettre power dans les variables et utiliser la fonction min_power
    gf=open(G, "r") 
    gf.readline() #on lit la première ligne car elle n'est pas utili
    gf=gf.readlines() #on lit toutes les lignes
    for i in range(0,len(gf)) :
         
        gf[i]=gf[i].split()
        if chemin != None and int(gf[i][0]) in chemin and int(gf[i][1]) in chemin :
            g.edge(gf[i][0], gf[i][1], color="green")
        else :
            g.edge(gf[i][0], gf[i][1])
    
    print(chemin)
    if chemin is not None : 
        for node in chemin : 
            g.node(str(node), color = 'blue')
    g.render()




