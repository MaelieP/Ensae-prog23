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

    """def makeset(self, node) :
        node.parent = node
        rank(node) = 0"""

    def find(self, node):
        while node.parent != node:
            node.parent = node
        print("Voici node.parent", node.parent)
        return node.parent
        
    def union(self, x, y):
        Rx = self.find(x)
        print("Voici Rx", Rx)
        Ry = self.find(y)
        print("Voici Ry", Ry)

        if Rx == Ry:
            return

        if Rx.rank < Ry.rank:
            Rx.parent = Ry
        elif Rx.rank > Ry.rank:
            Ry.parent = Rx
        else:
            Ry.parent = Rx
            Rx.rank += 1

    # Fonction pour trouver l'arbre couvrant minimum
    def kruskal(self):
        g_mst = []
        self.edges = sorted(self.edges, key=lambda edge: edge.power_min)

        for node in self.nodes:
            node.parent = node
            node.rank = 0

        for edge in self.edges:
            u = edge.u
            v = edge.v

            if self.find(u) != self.find(v):
                mst.append(edge)
                self.union(u, v)

        return g_mst

def temps(trajets,nom_fichier, n=2) :
    G=graph_from_file(nom_fichier)
    trajets=open(trajets)
    line=trajets.readline().split()
    nb=int(line[0])
    temp=[]
    i=0
    while i<=n :
        traj=random.randint(1,nb)
        for k in range(0, traj-1) :
            trajets.readline()
        line=trajets.readline().split()
        (src, dest)=(int(line[0]),int(line[1]))           
        t0=time.perf_counter()
        G.min_power(src, dest)
        t=time.perf_counter()-t0
        temp.append(t)
        i+=1
    print(mean(temp)*nb)
    return mean(temp)*nb
### IMPORT TRUC

    # Fonction pour unir deux arbres en utilisant la technique d'union par rang

    
#INSERE 
#def kuskral(g) : 

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



#import graphviz

"""def represente(G, src, dest, power=1) :
    graphe=graph_from_file(G)
    g=graphviz.Graph(filename='G', format='png', directory="delivery_network", engine='dot')
    chemin=graphe.get_path_with_power(src, dest, power )
    gf=open(G, "r")
    gf.readline()
    gf=gf.readlines()
    for i in range(0,len(gf)) :
         
        gf[i]=gf[i].split()
        if chemin != None and int(gf[i][0]) in chemin and int(gf[i][1]) in chemin :
            g.edge(gf[i][0], gf[i][1], color="green")
        else :
            g.edge(gf[i][0], gf[i][1])
    g.render()
G="input/network.00.in"
represente(G, 1, 2)"""



