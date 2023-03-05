# This will work if ran from the root folder.
import sys 
sys.path.append("delivery_network")

from graph import graph_from_file
import unittest   # The test framework

class Test_MinimalPower(unittest.TestCase):
    def test_network0(self):
        g = graph_from_file("/home/onyxia/work/Ensae-prog23/input/network.00.in")
        self.assertEqual(g.min_power(1, 4), 11)
        self.assertEqual(g.min_power(2, 4), 10)

    def test_network1(self):
        g = graph_from_file("/home/onyxia/work/Ensae-prog23/input/network.04.in")
        self.assertEqual(g.min_power(1, 4), 4)

if __name__ == '__main__':
    unittest.main()
