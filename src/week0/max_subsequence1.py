import sys


def construct_array(file_path):
    with open(file_path) as file:
        return sorted([int(line) for line in file])


def max_subsequence(array):
    current = 0
    maximum = 0

    for x in array:
        current = max(0, current + x)
        maximum = max(maximum, current)

    return maximum


def main(argv):
    array = construct_array(argv[0])
    size  = max_subsequence(array)

    print
    print 'Maximum Subsequence: %8d' % (size)
    print


if __name__ == "__main__":
    main(sys.argv[1:])
