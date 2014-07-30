import sys


def construct_array(file_path):
    with open(file_path) as file:
        return [int(line) for line in file]


def two_sum(array):
    array    = sorted(array)
    elements = []

    for index in range(len(array)):
        values = [element for element in array if (-10000 - array[index]) <= element <= (10000 - array[index])]
        elements.extend(values)
        sys.stdout.write('Found: %7d, Current: %7d [Index = %7d]\r' % (len(values), array[index], index))
        sys.stdout.flush()

    return len(set(elements))


def main(argv):
    array = construct_array(argv[0])
    count = two_sum(array)

    print '\n\nNumber of Ts with distinct solutions: %8d' % (count)


if __name__ == "__main__":
    main(sys.argv[1:])
