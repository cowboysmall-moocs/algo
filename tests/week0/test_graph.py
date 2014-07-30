import unittest
import os.path

from week0.graph import Graph


class TestGraph(unittest.TestCase):

    def test_adjacent_to(self):
        graph_dict = {}
        graph_dict[1] = [2, 3, 4]
        graph_dict[2] = [1, 3, 4]
        graph_dict[3] = [1, 2, 4]
        graph_dict[4] = [1, 2, 3]

        graph = Graph(graph_dict)

        self.assertEqual(graph.adjacent_to(1), [2, 3, 4])
        self.assertEqual(graph.adjacent_to(2), [1, 3, 4])
        self.assertEqual(graph.adjacent_to(3), [1, 2, 4])
        self.assertEqual(graph.adjacent_to(4), [1, 2, 3])


    def test_edges(self):
        graph_dict = {}
        graph_dict[1] = [2, 3, 4]
        graph_dict[2] = [1, 3, 4]
        graph_dict[3] = [1, 2, 4]
        graph_dict[4] = [1, 2, 3]

        graph = Graph(graph_dict)

        self.assertEqual(graph.edges(), [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)])


if __name__ == '__main__':
    unittest.main()
