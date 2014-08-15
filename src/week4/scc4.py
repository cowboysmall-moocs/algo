import sys

from collections import defaultdict


stack      = []
index      = {}
lowlink    = {}
statistics = defaultdict(int)

counter    = 0

def construct(file_path):
    graph = defaultdict(list)

    with open(file_path) as file:
        for line in file:
            item = line.split()
            graph[int(item[0])].append(int(item[1]))

    return graph


def scc(graph, v):
    global counter

    index[v]   = counter
    lowlink[v] = counter
    counter   += 1

    stack.append(v)

    for w in graph[v]:
        if w not in index:
            scc(graph, w)
            lowlink[v] = min(lowlink[v], lowlink[w])
        elif w in stack:
            lowlink[v] = min(lowlink[v], index[w])

    if lowlink[v] == index[v]:
        position       = stack.index(v)
        statistics[v] += len(stack[position:])
        print 'SCC found: ', stack[position:]
        del stack[position:]


def main(argv):
    sys.setrecursionlimit(1048576)

    graph = construct(argv[0])
    for v in graph.keys():
        if v not in index:
            scc(graph, v)

    print
    print 'Number of SCCs: %s' % len(statistics)
    print '    Top 5 SCCs: %s' % str(sorted(statistics.values(), reverse = True)[0:5])
    print


if __name__ == "__main__":
    main(sys.argv[1:])
