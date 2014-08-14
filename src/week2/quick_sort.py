import sys


class QuickSort:

    def __init__(self, array):
        self.array       = array
        self.comparisons = 0

    def get_comparisons(self):
        return self.comparisons

    def sort(self):
        self.quick_sort(self.array, 0, len(self.array))
        return self.array

    def quick_sort(self, array, start, end):
        if end - start < 2:
            return
        self.comparisons += (end - start - 1)
        self.pivot(array, start, end - 1)
        counter = start + 1;
        for index in xrange(start + 1, end):
            if array[index] < array[start]:
                self.swap_elements(array, index, counter)
                counter += 1
        self.swap_elements(array, start, counter - 1)
        self.quick_sort(array, start, counter - 1)
        self.quick_sort(array, counter, end)

    def pivot(self, array, start, end):
        return

    def swap_elements(self, array, a, b):
        temp     = array[a]
        array[a] = array[b]
        array[b] = temp


class QuickSortPivotLast(QuickSort):

    def pivot(self, array, start, end):
        self.swap_elements(array, start, end)


class QuickSortPivotMOT(QuickSort):

    def pivot(self, array, start, end):
        mid = int((start + end) / 2)

        if array[start] <= array[mid] <= array[end] or array[end] <= array[mid] <= array[start]:
            self.swap_elements(array, start, mid)
        elif array[mid] <= array[end] <= array[start] or array[start] <= array[end] <= array[mid]:
            self.swap_elements(array, start, end)
        else:
            return



def main(argv):
    file = open(argv[0])
    unsorted_list = [int(element) for element in file.readlines()]
    file.close()

    sorter      = QuickSort(unsorted_list)
    sorted_list = sorter.sort()
    comparisons = sorter.get_comparisons()
    print "file \'%s\' contained %s elements and was sorted with %s comparisons" % (argv[0], len(sorted_list), comparisons)


if __name__ == "__main__":
    main(sys.argv[1:])
