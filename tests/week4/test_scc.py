import unittest
import os.path

# from algorithms1.week4.scc import 


# FILE_1 = os.path.join(os.path.dirname(__file__), '../data/scc.txt')


class TestStronglyConnectedComponents(unittest.TestCase):

    def test_something_else(self):
        graph_dict = {}
        graph_dict[0] = [2, 3]
        graph_dict[1] = [0]
        graph_dict[2] = [1]
        graph_dict[3] = [4]
        graph_dict[4] = []


        reverse_graph_dict = {}
        reverse_graph_dict[0] = [1]
        reverse_graph_dict[1] = [2]
        reverse_graph_dict[2] = [0]
        reverse_graph_dict[3] = [0]
        reverse_graph_dict[4] = [3]

        self.assertEqual(len(graph_dict), 5)
        self.assertEqual(len(reverse_graph_dict), 5)
        # self.assertEqual(len(output), 3)
        # self.assertEqual(output, {0: [4], 1: [3], 2: [0, 2, 1]})
        # self.assertEqual(output, {0: [4], 1: [3], 2: [2, 1, 0]})

