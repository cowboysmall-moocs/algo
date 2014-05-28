import unittest
import os.path

from algorithms1.week4.dfs import DFS


# FILE_1 = os.path.join(os.path.dirname(__file__), '../data/scc.txt')


class TestStronglyConnectedComponents(unittest.TestCase):

    def test_simple(self):
        graph_dict = {}
        graph_dict[3] = []
        graph_dict[2] = [3]
        graph_dict[1] = [2]
        graph_dict[0] = [1]
        self.assertEqual(DFS(graph_dict).dfs(), [0, 1, 2, 3])

    def test_something(self):
        graph_dict = {}
        graph_dict[0] = [1, 2]
        graph_dict[1] = [2, 3]
        graph_dict[2] = [3]
        graph_dict[3] = [1]
        self.assertEqual(DFS(graph_dict).dfs(), [0, 1, 2, 3])

    def test_something_else(self):
        graph_dict = {}
        graph_dict[2] = [1]
        graph_dict[4] = []
        graph_dict[0] = [2, 3]
        graph_dict[1] = [0]
        graph_dict[3] = [4]
        self.assertEqual(DFS(graph_dict).dfs(), [0, 3, 4, 2, 1])

    def test_something_other(self):
        graph_dict = {}
        graph_dict[0] = [3, 4]
        graph_dict[1] = [3]
        graph_dict[2] = [4, 7]
        graph_dict[3] = [5, 6, 7]
        graph_dict[4] = [6]
        graph_dict[5] = []
        graph_dict[6] = []
        graph_dict[7] = []
        self.assertEqual(DFS(graph_dict).dfs(), [2, 1, 0, 4, 3, 7, 6, 5])



if __name__ == '__main__':
    unittest.main()
