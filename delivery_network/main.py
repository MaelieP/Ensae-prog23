from graph import Graph, graph_from_file


data_path = "input/"
file_name = "network.01.in"

g = graph_from_file(data_path + file_name)
print(g)

#Crée un nouvel objet de la classe graphe pour tester
"g = Graph([1])"
"print(g)"
#piour exécuter  : terminal 
"g.add_edge(2, 1, 18)"
"print(g.nodes)"