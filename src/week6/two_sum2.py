import sys

from bisect import bisect_left, bisect_right


def construct_array(file_path):
    with open(file_path) as file:
        return sorted([int(line) for line in file])


def two_sum(array):
    two_sums = set()

    for x in array:
        start = bisect_left(array, -10000 - x)
        end   = bisect_right(array, 10000 - x)
        while start < end:
            two_sums.add(x + array[start])
            start += 1

    return len(two_sums)


def main(argv):
    array = construct_array(argv[0])
    count = two_sum(array)

    print
    print 'Number of Ts with distinct solutions: %8d' % (count)
    print


if __name__ == "__main__":
    main(sys.argv[1:])
