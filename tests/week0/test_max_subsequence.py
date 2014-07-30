import unittest
import os.path

from week0.max_subsequence2 import max_subsequence


class TestMaxSubsequence(unittest.TestCase):

    def test_basic(self):
        size = max_subsequence([1, 4, -2, -4, 6, 9, -3, 8, 4, -2, 9, 13, -12, -33, 17, -99])
        self.assertEqual(size[0],  4)
        self.assertEqual(size[1], 11)
        self.assertEqual(size[2], 44)

        size = max_subsequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        self.assertEqual(size[0], 3)
        self.assertEqual(size[1], 6)
        self.assertEqual(size[2], 6)
