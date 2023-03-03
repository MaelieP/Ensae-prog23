# À compléter
# This will work if ran from the root folder.
import sys 
sys.path.append("delivery_network")

from graph import Graph, graph_from_file

import unittest
g = graph_from_file("/home/onyxia/work/Ensae-prog23/input/network.00.in")
g.min_power(1,4)