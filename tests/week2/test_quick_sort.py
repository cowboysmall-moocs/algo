import unittest
import os.path

from week2.quick_sort import QuickSort, QuickSortPivotLast, QuickSortPivotMOT

FILE_1 = os.path.join(os.path.dirname(__file__), '../data/unsorted_list.txt')
FILE_2 = os.path.join(os.path.dirname(__file__), '../data/unsorted_list_10.txt')
FILE_3 = os.path.join(os.path.dirname(__file__), '../data/unsorted_list_100.txt')
FILE_4 = os.path.join(os.path.dirname(__file__), '../data/unsorted_list_1000.txt')


class TestQuickSort(unittest.TestCase):


    def test_basic_quicksort_empty(self):
        sorter = QuickSort([])
        self.assertEqual(sorter.sort(), [])
        self.assertEqual(sorter.get_comparisons(), 0)


    def test_pivot_last_quicksort_empty(self):
        sorter = QuickSortPivotLast([])
        self.assertEqual(sorter.sort(), [])
        self.assertEqual(sorter.get_comparisons(), 0)


    def test_mot_quicksort_empty(self):
        sorter = QuickSortPivotMOT([])
        self.assertEqual(sorter.sort(), [])
        self.assertEqual(sorter.get_comparisons(), 0)


    def test_basic_quicksort_one_element(self):
        sorter = QuickSort([1])
        self.assertEqual(sorter.sort(), [1])
        self.assertEqual(sorter.get_comparisons(), 0)


    def test_pivot_last_quicksort_one_element(self):
        sorter = QuickSortPivotLast([1])
        self.assertEqual(sorter.sort(), [1])
        self.assertEqual(sorter.get_comparisons(), 0)


    def test_mot_quicksort_one_element(self):
        sorter = QuickSortPivotMOT([1])
        self.assertEqual(sorter.sort(), [1])
        self.assertEqual(sorter.get_comparisons(), 0)


    def test_basic_quicksort_odd_length(self):
        sorter = QuickSort([3, 6, 2, 7, 9])
        self.assertEqual(sorter.sort(), [2, 3, 6, 7, 9])
        self.assertEqual(sorter.get_comparisons(), 7)


    def test_pivot_last_quicksort_odd_length(self):
        sorter = QuickSortPivotLast([3, 6, 2, 7, 9])
        self.assertEqual(sorter.sort(), [2, 3, 6, 7, 9])
        self.assertEqual(sorter.get_comparisons(), 10)


    def test_mot_quicksort_odd_length(self):
        sorter = QuickSortPivotMOT([3, 6, 2, 7, 9])
        self.assertEqual(sorter.sort(), [2, 3, 6, 7, 9])
        self.assertEqual(sorter.get_comparisons(), 6)


    def test_basic_quicksort_ten_elements(self):
        sorter = QuickSort([8, 3, 6, 10, 2, 7, 9, 4, 1, 5])
        self.assertEqual(sorter.get_comparisons(), 0)
        self.assertEqual(sorter.sort(), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(sorter.get_comparisons(), 22)


    def test_pivot_last_quicksort_ten_elements(self):
        sorter = QuickSortPivotLast([8, 3, 6, 10, 2, 7, 9, 4, 1, 5])
        self.assertEqual(sorter.get_comparisons(), 0)
        self.assertEqual(sorter.sort(), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(sorter.get_comparisons(), 20)


    def test_mot_quicksort_ten_elements(self):
        sorter = QuickSortPivotMOT([8, 3, 6, 10, 2, 7, 9, 4, 1, 5])
        self.assertEqual(sorter.get_comparisons(), 0)
        self.assertEqual(sorter.sort(), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(sorter.get_comparisons(), 19)


    def test_basic_quicksort_twenty_elements(self):
        sorter = QuickSort([18, 8, 15, 12, 16, 3, 20, 6, 17, 11, 10, 2, 19, 7, 14, 9, 4, 1, 5, 13])
        self.assertEqual(sorter.sort(), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
        self.assertEqual(sorter.get_comparisons(), 71)


    def test_pivot_last_quicksort_twenty_elements(self):
        sorter = QuickSortPivotLast([18, 8, 15, 12, 16, 3, 20, 6, 17, 11, 10, 2, 19, 7, 14, 9, 4, 1, 5, 13])
        self.assertEqual(sorter.sort(), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
        self.assertEqual(sorter.get_comparisons(), 65)


    def test_mot_quicksort_twenty_elements(self):
        sorter = QuickSortPivotMOT([18, 8, 15, 12, 16, 3, 20, 6, 17, 11, 10, 2, 19, 7, 14, 9, 4, 1, 5, 13])
        self.assertEqual(sorter.sort(), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
        self.assertEqual(sorter.get_comparisons(), 57)


    def test_basic_quicksort_file_1(self):
        file = open(FILE_1)
        unsorted = [int(element) for element in file.readlines()]
        file.close()

        sorter = QuickSort(unsorted)
        sorted_list = sorter.sort()

        self.assertEqual(len(sorted_list), 10000)
        self.assertEqual(sorter.get_comparisons(), 162085)


    def test_pivot_last_quicksort_file_1(self):
        file = open(FILE_1)
        unsorted = [int(element) for element in file.readlines()]
        file.close()

        sorter = QuickSortPivotLast(unsorted)
        sorted_list = sorter.sort()

        self.assertEqual(len(sorted_list), 10000)
        self.assertEqual(sorter.get_comparisons(), 164123)


    def test_mot_quicksort_file_1(self):
        file = open(FILE_1)
        unsorted = [int(element) for element in file.readlines()]
        file.close()

        sorter = QuickSortPivotMOT(unsorted)
        sorted_list = sorter.sort()

        self.assertEqual(len(sorted_list), 10000)
        self.assertEqual(sorter.get_comparisons(), 138382)

    def test_basic_quicksort_file_2(self):
        file = open(FILE_2)
        unsorted = [int(element) for element in file.readlines()]
        file.close()

        sorter = QuickSort(unsorted)
        sorted_list = sorter.sort()

        self.assertEqual(len(sorted_list), 10)
        self.assertEqual(sorter.get_comparisons(), 25)


    def test_pivot_last_quicksort_file_2(self):
        file = open(FILE_2)
        unsorted = [int(element) for element in file.readlines()]
        file.close()

        sorter = QuickSortPivotLast(unsorted)
        sorted_list = sorter.sort()

        self.assertEqual(len(sorted_list), 10)
        self.assertEqual(sorter.get_comparisons(), 29)


    def test_mot_quicksort_file_2(self):
        file = open(FILE_2)
        unsorted = [int(element) for element in file.readlines()]
        file.close()

        sorter = QuickSortPivotMOT(unsorted)
        sorted_list = sorter.sort()

        self.assertEqual(len(sorted_list), 10)
        self.assertEqual(sorter.get_comparisons(), 21)

    def test_basic_quicksort_file_3(self):
        file = open(FILE_3)
        unsorted = [int(element) for element in file.readlines()]
        file.close()

        sorter = QuickSort(unsorted)
        sorted_list = sorter.sort()

        self.assertEqual(len(sorted_list), 100)
        self.assertEqual(sorter.get_comparisons(), 615)


    def test_pivot_last_quicksort_file_3(self):
        file = open(FILE_3)
        unsorted = [int(element) for element in file.readlines()]
        file.close()

        sorter = QuickSortPivotLast(unsorted)
        sorted_list = sorter.sort()

        self.assertEqual(len(sorted_list), 100)
        self.assertEqual(sorter.get_comparisons(), 587)


    def test_mot_quicksort_file_3(self):
        file = open(FILE_3)
        unsorted = [int(element) for element in file.readlines()]
        file.close()

        sorter = QuickSortPivotMOT(unsorted)
        sorted_list = sorter.sort()

        self.assertEqual(len(sorted_list), 100)
        self.assertEqual(sorter.get_comparisons(), 518)

    def test_basic_quicksort_file_4(self):
        file = open(FILE_4)
        unsorted = [int(element) for element in file.readlines()]
        file.close()

        sorter = QuickSort(unsorted)
        sorted_list = sorter.sort()

        self.assertEqual(len(sorted_list), 1000)
        self.assertEqual(sorter.get_comparisons(), 10297)


    def test_pivot_last_quicksort_file_4(self):
        file = open(FILE_4)
        unsorted = [int(element) for element in file.readlines()]
        file.close()

        sorter = QuickSortPivotLast(unsorted)
        sorted_list = sorter.sort()

        self.assertEqual(len(sorted_list), 1000)
        self.assertEqual(sorter.get_comparisons(), 10184)


    def test_mot_quicksort_file_4(self):
        file = open(FILE_4)
        unsorted = [int(element) for element in file.readlines()]
        file.close()

        sorter = QuickSortPivotMOT(unsorted)
        sorted_list = sorter.sort()

        self.assertEqual(len(sorted_list), 1000)
        self.assertEqual(sorter.get_comparisons(), 8921)


if __name__ == '__main__':
    unittest.main()
