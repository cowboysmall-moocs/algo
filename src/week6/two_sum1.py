import sys


def construct_hash_table(file_path):
    hash_table = {}

    with open(file_path) as file:
        for line in file:
            hash_table[int(line)] = 0

    return hash_table


def two_sum(hash_table):
    counter   = 0
    hash_keys = hash_table.keys()

    for val in xrange(-10000, 10001):
        for key in hash_keys:
            target = val - key
            if target != key and target in hash_table:
                counter += 1
                break

    return counter


def main(argv):
    hash_table = construct_hash_table(argv[0])
    count      = two_sum(hash_table)

    print
    print 'Number of Ts with distinct solutions: %8d' % (count)
    print


if __name__ == "__main__":
    main(sys.argv[1:])
