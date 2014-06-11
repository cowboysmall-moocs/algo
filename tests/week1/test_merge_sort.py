import unittest
import os.path
import random

from week1.merge_sort import MergeSort

FILE_1 = os.path.join(os.path.dirname(__file__), '../data/integer_array_1.txt')
FILE_2 = os.path.join(os.path.dirname(__file__), '../data/integer_array_2.txt')
FILE_3 = os.path.join(os.path.dirname(__file__), '../data/integer_array_3.txt')
FILE_4 = os.path.join(os.path.dirname(__file__), '../data/integer_array_4.txt')
FILE_5 = os.path.join(os.path.dirname(__file__), '../data/integer_array_5.txt')
FILE_6 = os.path.join(os.path.dirname(__file__), '../data/integer_array_6.txt')


class TestMergeSort(unittest.TestCase):


    def test_basic_sort_empty(self):
        self.assertEqual(MergeSort([]).sort(), [])


    def test_basic_sort_one_element(self):
        self.assertEqual(MergeSort([1]).sort(), [1])


    def test_basic_sort_odd_length(self):
        self.assertEqual(MergeSort([3, 6, 2, 7, 9]).sort(), [2, 3, 6, 7, 9])


    def test_basic_sort_even_length(self):
        self.assertEqual(MergeSort([8, 3, 6, 10, 2, 7, 9, 4, 1, 5]).sort(), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


    def test_sort_small_random(self):
        small_random_array  = [random.random() for _ in xrange(100)]
        sorted = MergeSort(small_random_array).sort()
        self.assertEqual(len(sorted), len(small_random_array))


    def test_sort_medium_random(self):
        medium_random_array = [random.random() for _ in xrange(10000)]
        sorted = MergeSort(medium_random_array).sort()
        self.assertEqual(len(sorted), len(medium_random_array))


    def test_sort_large_random(self):
        large_random_array  = [random.random() for _ in xrange(100000)]
        sorted = MergeSort(large_random_array).sort()
        self.assertEqual(len(sorted), len(large_random_array))


    def test_sort_and_count_empty(self):
        unsorted = []

        sorter = MergeSort(unsorted)
        sorted = sorter.sort()
        count  = sorter.get_inversions()

        self.assertEqual(count, 0)
        self.assertEqual(sorted, [])


    def test_sort_and_count_one_element(self):
        unsorted = [0]

        sorter = MergeSort(unsorted)
        sorted = sorter.sort()
        count  = sorter.get_inversions()

        self.assertEqual(count, 0)
        self.assertEqual(sorted, [0])


    def test_sort_and_count_one_element_max_int(self):
        unsorted = [4294967295]

        sorter = MergeSort(unsorted)
        sorted = sorter.sort()
        count  = sorter.get_inversions()

        self.assertEqual(count, 0)
        self.assertEqual(sorted, [4294967295])


    def test_sort_and_count_two_elements(self):
        unsorted = [0, 0]

        sorter = MergeSort(unsorted)
        sorted = sorter.sort()
        count  = sorter.get_inversions()

        self.assertEqual(count, 0)
        self.assertEqual(sorted, [0, 0])


    def test_sort_and_count_two_elements_basic_split(self):
        unsorted = [1, 0]

        sorter = MergeSort(unsorted)
        sorted = sorter.sort()
        count  = sorter.get_inversions()

        self.assertEqual(count, 1)
        self.assertEqual(sorted, [0, 1])


    def test_sort_and_count_three_elements_basic_split(self):
        unsorted = [1, 1, 0]

        sorter = MergeSort(unsorted)
        sorted = sorter.sort()
        count  = sorter.get_inversions()

        self.assertEqual(count, 2)
        self.assertEqual(sorted, [0, 1, 1])


    def test_sort_and_count_four_elements_left_split(self):
        unsorted = [1, 0, 1, 1]

        sorter = MergeSort(unsorted)
        sorted = sorter.sort()
        count  = sorter.get_inversions()

        self.assertEqual(count, 1)
        self.assertEqual(sorted, [0, 1, 1, 1])


    def test_sort_and_count_four_elements_right_split(self):
        unsorted = [0, 0, 1, 0]

        sorter = MergeSort(unsorted)
        sorted = sorter.sort()
        count  = sorter.get_inversions()

        self.assertEqual(count, 1)
        self.assertEqual(sorted, [0, 0, 0, 1])


    def test_sort_and_count_four_elements_left_and_right_splits(self):
        unsorted = [1, 0, 1, 0]

        sorter = MergeSort(unsorted)
        sorted = sorter.sort()
        count  = sorter.get_inversions()

        self.assertEqual(count, 3)
        self.assertEqual(sorted, [0, 0, 1, 1])


    def test_sort_and_count_file_1(self):
        file = open(FILE_1)
        unsorted = [int(element) for element in file.readlines()]
        file.close()

        sorter = MergeSort(unsorted)
        sorted = sorter.sort()
        count  = sorter.get_inversions()

        self.assertEqual(count, 0)
        self.assertEqual(len(sorted), 6)


    def test_sort_and_count_file_2(self):
        file = open(FILE_2)
        unsorted = [int(element) for element in file.readlines()]
        file.close()

        sorter = MergeSort(unsorted)
        sorted = sorter.sort()
        count  = sorter.get_inversions()

        self.assertEqual(count, 3)
        self.assertEqual(len(sorted), 6)


    def test_sort_and_count_file_3(self):
        file = open(FILE_3)
        unsorted = [int(element) for element in file.readlines()]
        file.close()

        sorter = MergeSort(unsorted)
        sorted = sorter.sort()
        count  = sorter.get_inversions()

        self.assertEqual(count, 5)
        self.assertEqual(len(sorted), 6)


    def test_sort_and_count_file_4(self):
        file = open(FILE_4)
        unsorted = [int(element) for element in file.readlines()]
        file.close()

        sorter = MergeSort(unsorted)
        sorted = sorter.sort()
        count  = sorter.get_inversions()

        self.assertEqual(count, 15)
        self.assertEqual(len(sorted), 6)


    def test_sort_and_count_file_5(self):
        file = open(FILE_5)
        unsorted = [int(element) for element in file.readlines()]
        file.close()

        sorter = MergeSort(unsorted)
        sorted = sorter.sort()
        count  = sorter.get_inversions()

        self.assertEqual(count, 12)
        self.assertEqual(len(sorted), 10)


    def test_sort_and_count_file_6(self):
        file = open(FILE_6)
        unsorted = [int(element) for element in file.readlines()]
        file.close()

        sorter = MergeSort(unsorted)
        sorted = sorter.sort()
        count  = sorter.get_inversions()

        self.assertEqual(count, 2407905288)
        self.assertEqual(len(sorted), 100000)


if __name__ == '__main__':
    unittest.main()
