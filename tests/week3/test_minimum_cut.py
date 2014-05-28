import unittest
import os.path

from algorithms1.week3.graph import Graph


FILE_1 = os.path.join(os.path.dirname(__file__), '../data/karger_min_cut.txt')


class TestMinimumCut(unittest.TestCase):

    def test_something(self):
        file = open(FILE_1)
        adjacency_list = [element.strip('\t\r\n').split('\t') for element in file.readlines()]
        file.close()

        graph_dict = {}
        for row in adjacency_list:
            graph_dict[row[0]] = row[1:]

        graph = Graph(graph_dict)
        self.assertEqual(graph.adjacent_to('3'), ['48','123','134','109','41','17','159','49','136','16','130','141','29','176','2','190','66','153','157','70','114','65','173','104','194','54'])




if __name__ == '__main__':
    unittest.main()
