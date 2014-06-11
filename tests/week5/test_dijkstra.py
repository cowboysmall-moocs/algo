import unittest
import os.path

from week5.dijkstra import construct_graph, dijkstra_shortest_paths


FILE_1 = os.path.join(os.path.dirname(__file__), '../data/dijkstra_data.txt')


class TestDijkstra(unittest.TestCase):

    def test_solution(self):
        distances = dijkstra_shortest_paths(1, construct_graph(FILE_1))

        self.assertEqual(distances[7],   2599)
        self.assertEqual(distances[37],  2610)
        self.assertEqual(distances[59],  2947)
        self.assertEqual(distances[82],  2052)
        self.assertEqual(distances[99],  2367)
        self.assertEqual(distances[115], 2399)
        self.assertEqual(distances[133], 2029)
        self.assertEqual(distances[165], 2442)
        self.assertEqual(distances[188], 2505)
        self.assertEqual(distances[197], 3068)
