import sys
import heapq


def construct_stream(file_path):
    with open(file_path) as file:
        return [int(line) for line in file]


def median_maintenance(stream):
    total = 0
    upper, lower = [], []
    for integer in stream:
        if not lower or integer < -lower[0]:
            heapq.heappush(lower, -integer)
        else:
            heapq.heappush(upper, integer)

        difference = len(upper) - len(lower)
        if difference > 1:
            heapq.heappush(lower, -heapq.heappop(upper))
        elif difference < -1:
            heapq.heappush(upper, -heapq.heappop(lower))

        if len(upper) > len(lower):
            total += upper[0]
        else:
            total += -lower[0]
    return total


def main(argv):
    sum_of_medians = median_maintenance(construct_stream(argv[0]))

    print 'Sum of medians             = %8d' % (sum_of_medians)
    print 'Sum of medians (mod 10000) = %8d' % (sum_of_medians % 10000)


if __name__ == "__main__":
    main(sys.argv[1:])
