import sys


def construct_hash_table(file_path):
    hash_table = {}
    with open(file_path) as file:
        for line in file:
            hash_table[int(line)] = 0
    return hash_table


def main(argv):
    counter = 0
    hash_table = construct_hash_table(argv[0])
    hash_keys  = hash_table.keys()
    for val in range(-10000, 100001):
        sys.stdout.write('trying for T = %6d [running total = %6d]\r' % (val, counter))
        sys.stdout.flush()
        for number in hash_keys:
            target = val - number
            if target != number and target in hash_table:
                # hash_table[number] += 1
                # hash_table[target] += 1
                counter += 1
                # sys.stdout.write('\n\nfound for t = %6d [running total = %6d]\n\n' % (val, counter))
                # sys.stdout.flush()
                break

    print '\n\nCount of Ts with distinct solutions -> ', counter




if __name__ == "__main__":
    main(sys.argv[1:])
