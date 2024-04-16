import unittest
from graphs_2 import *


class TestClass(unittest.TestCase):
    def test_find_min_trail(self):
        graph = nx.MultiDiGraph()
        graph.add_weighted_edges_from([(1, 3, 0.1)])
        graph.add_weighted_edges_from([(1, 2, 0.5)])
        graph.add_weighted_edges_from([(2, 3, 0.4)])
        graph.add_weighted_edges_from([(2, 3, 0.3)])
        graph.add_weighted_edges_from([(2, 4, 0.3)])
        graph.add_weighted_edges_from([(2, 4, 0.3)])
        graph.add_weighted_edges_from([(4, 5, 0.1)])
        graph.add_weighted_edges_from([(5, 3, 0.1)])
        graph.add_weighted_edges_from([(3, 5, 0.2)])
        graph.add_weighted_edges_from([(5, 6, 0.2)])
        my_func = find_min_trail(graph, 1, 6)
        my_weight = 0
        for i in range(len(my_func)):
            my_weight += my_func[i].weight
        nx_weight = nx.dijkstra_path_length(graph, 1, 6)

        self.assertEqual(nx_weight, my_weight)


if __name__ == '__main__':
    unittest.main()
