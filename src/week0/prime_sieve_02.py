import sys
import math


def main(argv):
    maximum = int(argv[0])

    markers = [True] * (maximum + 1)
    primes  = []
    for i in xrange(2, maximum + 1):
        if markers[i]:
            primes.append(i)
            for j in xrange(i ** 2, maximum + 1, i):
                markers[j] = False

    count   = len(primes)


    print
    print'    Total primes between 2 and %s: %s' % (maximum, count)
    print'Total composites between 2 and %s: %s' % (maximum, maximum - 1 - count)
    print
    print '\n'.join([', '.join(['%4s' % p for p in primes[k:k + 10]]) for k in xrange(0, len(primes), 10)])
    print


if __name__ == "__main__":
    main(sys.argv[1:])
