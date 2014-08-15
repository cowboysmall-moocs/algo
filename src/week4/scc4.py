import sys

from collections import defaultdict


stack      = []
index      = {}
lowlink    = {}
statistics = defaultdict(int)

counter    = 0

def construct(file_path):
    vertices = []
    graph    = defaultdict(list)

    with open(file_path) as file:
        for line in file:
            item = line.split()
            tail = int(item[0])
            head = int(item[1])
            graph[tail].append(head)
            vertices.extend([tail, head])

    return graph, vertices


def scc(v, graph):
    global counter

    index[v]   = counter
    lowlink[v] = counter
    counter   += 1

    stack.append(v)

    for w in graph[v]:
        if w not in index:
            scc(w, graph)
            lowlink[v] = min(lowlink[v], lowlink[w])
        elif w in stack:
            lowlink[v] = min(lowlink[v], index[w])

    if lowlink[v] == index[v]:
        while v in stack:
            statistics[v] += 1
            stack.pop()


def main(argv):
    graph, vertices = construct(argv[0])

    sys.setrecursionlimit(1048576)

    for v in vertices:
        if v not in index:
            scc(v, graph)

    print
    print 'Top 5 SCCs: %s' % str(sorted(statistics.values(), reverse = True)[0:5])
    print


if __name__ == "__main__":
    main(sys.argv[1:])
