import sys

def construct_array(file_path):
    with open(file_path) as file:
        return sorted([int(line) for line in file])


def max_subsequence(array):
    current = 0
    maximum = 0

    start   = 0
    end     = 0
    pointer = 0

    for index in range(len(array)):
        if current < 0:
            current = array[index]
            pointer = index
        else:
            current += array[index]

        if maximum < current:
            maximum = current
            start   = pointer
            end     = index

    return start, end, maximum


def main(argv):
    array   = construct_array(argv[0])
    s, e, m = max_subsequence(array)

    print
    print 'Maximum Subsequence [%s, %s] : %8d' % (s, e, m)
    print

if __name__ == "__main__":
    main(sys.argv[1:])
