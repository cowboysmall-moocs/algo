import unittest

from week0.union_find import QuickFind, WeightedQuickUnion

class TestUnionFind(unittest.TestCase):

    def test_first_case(self):
        find = QuickFind(10)
        # 6-0 8-3 6-7 7-5 0-9 4-5 

        find.union(6, 0)
        find.union(8, 3)
        find.union(6, 7)
        find.union(7, 5)
        find.union(0, 9)
        find.union(4, 5)

        self.assertEqual(find.get_array(), [9, 1, 2, 3, 9, 9, 9, 9, 3, 9])
        

    def test_second_case(self):
        find = QuickFind(10)
        # 7-8 7-4 4-1 5-9 2-0 6-1 

        find.union(7, 8)
        find.union(7, 4)
        find.union(4, 1)
        find.union(5, 9)
        find.union(2, 0)
        find.union(6, 1)

        self.assertEqual(find.get_array(), [0, 1, 0, 3, 1, 9, 1, 1, 1, 9])


    def test_third_case(self):
        find = QuickFind(10)
         # 1-2 9-8 8-5 3-1 6-3 8-0 

        find.union(1, 2)
        find.union(9, 8)
        find.union(8, 5)
        find.union(3, 1)
        find.union(6, 3)
        find.union(8, 0)

        self.assertEqual(find.get_array(), [0, 2, 2, 2, 4, 0, 2, 7, 0, 0])


    def test_fourth_case(self):
        find = WeightedQuickUnion(10)
        # 3-6 2-6 8-6 1-4 2-7 0-5 5-1 2-4 5-9

        find.union(3, 6)
        find.union(2, 6)
        find.union(8, 6)
        find.union(1, 4)
        find.union(2, 7)
        find.union(0, 5)
        find.union(5, 1)
        find.union(2, 4)
        find.union(5, 9)

        self.assertEqual(find.get_array(), [3, 0, 3, 3, 1, 0, 3, 3, 3, 3])
        self.assertEqual(find.get_sizes(), [4, 2, 1, 10, 1, 1, 1, 1, 1, 1])
        

    def test_fifth_case(self):
        find = WeightedQuickUnion(10)
        # 9-7 5-1 2-8 6-3 5-8 3-7 8-4 8-0 9-0

        find.union(9, 7)
        find.union(5, 1)
        find.union(2, 8)
        find.union(6, 3)
        find.union(5, 8)
        find.union(3, 7)
        find.union(8, 4)
        find.union(8, 0)
        find.union(9, 0)

        self.assertEqual(find.get_array(), [5, 5, 5, 6, 5, 5, 5, 9, 2, 6])
        self.assertEqual(find.get_sizes(), [1, 1, 2, 1, 1, 10, 4, 1, 1, 2])


    def test_sixth_case(self):
        find = WeightedQuickUnion(10)
        # 5-4 0-9 8-5 7-6 2-5 4-1 0-7 7-8 7-3

        find.union(5, 4)
        find.union(0, 9)
        find.union(8, 5)
        find.union(7, 6)
        find.union(2, 5)
        find.union(4, 1)
        find.union(0, 7)
        find.union(7, 8)
        find.union(7, 3)

        self.assertEqual(find.get_array(), [5, 5, 5, 5, 5, 5, 7, 0, 5, 0])
        self.assertEqual(find.get_sizes(), [4, 1, 1, 1, 1, 10, 1, 2, 1, 1])

