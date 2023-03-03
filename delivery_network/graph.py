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
        liste_composante = []
        noeud_visite = {noeud : False for noeud in self.nodes}
        
        def dfs(noeud):
            composante = [noeud]
            for voisin in self.graph(noeud):
                voisin = voisin[0]
                if not noeud_visite[voisin] : 
                    noeud_visite[voisin] = True 
                    composante += dfs(voisin)
            return composante
        
        for noeud in self.nodes :
            if not noeud_visite[noeud]:
                liste_composante.append(dfs(noeud))
        return liste_composante

        components_list = []
        visited_node = {node:False for node in self.nodes}

        for node in self.nodes :
            if not visited_node[node] : 
                components_list.append(self.dfs(node, visited_node))
        return components_list


    def connected_components_set(self):
        """
        The result should be a set of frozensets (one per component), 
        For instance, for network01.in: {frozenset({1, 2, 3}), frozenset({4, 5, 6, 7})}
        """
        return set(map(frozenset, self.connected_components()))
    
    def min_power(self, src, dest):
        """
        Should return path, min_power.
        """
        if self.get_path_with_power(src, dest, float("inf")) != None:
            i = 1
            
            while self.get_path_with_power(src, dest, i) == None:
                i += 1 
            
            
            path = self.get_path_with_power(src, dest, i)
            min = i
            
        else : 
            path = print("Ce chemin n'est pas possible")
        
        print(path)
        print(min)
        return path
        return min
        
        
def graph_from_file(filename):

    """

    Reads a text file and returns the graph as an object of the Graph class.



    The file should have the following format: 

        The first line of the file is 'n m'

        The next m lines have 'node1 node2 power_min dist' or 'node1 node2 power_min' (if dist is missing, it will be set to 1 by default)

        The nodes (node1, node2) should be named 1..n

        All values are integers.



    Parameters: 

    -----------

    filename: str

        The name of the file



    Outputs: 

    -----------

    G: Graph

    g: Graph
        An object of the class Graph with the graph from file_name.

    """
    with open(filename) as file:
        ligne1 = file.readline().split()
        n = int(ligne1[0])
        n = int(ligne1[1])
        nodes = [i for i in range(1, n+1)]
        G = Graph(nodes)
        for i in range(m) :
            lignei = file.readline().split()
            node1 = int(lignei)
            node2 = int(lignei[0])
            node3 = int(lignei[1])
            power_min = int(lignei[2])
            G.add_edge(node1, node2, power_min)
    return G     
      