import sys


def main(argv):
    a = [0] * 1000000
    t = 0
    modulus = 2 ** 24

    for i in xrange(1000000):
        t = (615949 * t + 797807) % modulus
        a[i] = t - modulus / 2

    for i in (20, 100, 1000, 10000, 100000, 1000000):
        fname = "two_sum_test%d.txt" % i
        f = open(fname, "w")
        for j in xrange(i):
            f.write("%d\n" % a[j])
        f.close()


if __name__ == "__main__":
    main(sys.argv[1:])
