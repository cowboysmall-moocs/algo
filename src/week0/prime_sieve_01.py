import sys
import math


def main(argv):
    maximum = int(argv[0])

    markers = [True] * (maximum + 1)
    for i in xrange(2, int(math.sqrt(maximum)) + 1):
        if markers[i]:
            for j in range(i ** 2, maximum + 1, i):
                markers[j] = False

    primes  = [p for p in xrange(2, maximum + 1) if markers[p]]
    count   = len(primes)


    print
    print'    Total primes between 2 and %s: %s' % (maximum, count)
    print'Total composites between 2 and %s: %s' % (maximum, maximum - 1 - count)
    # print
    # print', '.join([str(p) for p in primes])
    print


if __name__ == "__main__":
    main(sys.argv[1:])
