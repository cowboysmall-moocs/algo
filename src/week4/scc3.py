import sys

from collections import defaultdict


stack      = []
index      = {}
lowlink    = {}
components = defaultdict(list)


def construct(file_path):
    graph = defaultdict(list)

    with open(file_path) as file:
        for line in file:
            item = line.split()
            graph[int(item[0])].append(int(item[1]))

    return graph



def scc(v, graph, i):
    index[v]   = i
    lowlink[v] = i

    stack.append(v)

    for w in graph[v]:
        if w not in index:
            scc(w, graph, i + 1)
            lowlink[v] = min(lowlink[v], lowlink[w])
        elif w in stack:
            lowlink[v] = min(lowlink[v], index[w])

    if lowlink[v] == index[v]:
        # while v not in components[v]:
        while v in stack:
            components[v].append(stack.pop())


def main(argv):
    graph = construct(argv[0])

    sys.setrecursionlimit(1048576)

    for v in graph.keys():
        if v not in index:
            scc(v, graph, 0)

    stats = sorted([len(values) for values in components.values()], reverse = True)

    print
    print 'Top 5 SCCs: %s' % str(stats[0:5])
    print


if __name__ == "__main__":
    main(sys.argv[1:])
