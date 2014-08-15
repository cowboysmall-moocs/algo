import sys

from collections import defaultdict


explored   = defaultdict(bool)
leaders    = defaultdict(int)
finishing  = defaultdict(int)
components = defaultdict(list)


def construct_graphs(file_path):
    vertices       = []
    graph          = defaultdict(list)
    reversed_graph = defaultdict(list)

    with open(file_path) as file:
        for line in file:
            split = line.split()
            tail  = int(split[0])
            head  = int(split[1])
            graph[tail].append(head)
            reversed_graph[head].append(tail)
            vertices.extend([tail, head])

    return graph, reversed_graph, vertices


def reinitialize():
    global explored
    global leaders
    global finishing
    global components

    explored   = defaultdict(bool)
    leaders    = defaultdict(int)
    finishing  = defaultdict(int)
    components = defaultdict(list)


def dfs_loop(graph, vertex):
    global t

    explored[vertex] = True
    leaders[vertex]  = s
    components[s].append(vertex)

    if vertex in graph:
        for node in graph[vertex]:
            if not explored[node]:
                dfs_loop(graph, node)

    t = t + 1
    finishing[vertex] = t


def dfs(graph, node_count):
    global t
    global s

    t = 0
    s = 0

    for node in xrange(node_count, 0, -1):
        if not explored[node]:
            s = node
            dfs_loop(graph, node)


def relabel_graph(graph, node_count):
    relabeled_graph = {}

    for node in xrange(1, node_count + 1):
        relabeled_heads = []
        for head in graph[node]: 
            relabeled_heads.append(finishing[head])
        relabeled_graph[finishing[node]] = relabeled_heads

    return relabeled_graph


def scc(graph, reversed_graph, node_count):
    dfs(reversed_graph, node_count)

    relabeled_graph = relabel_graph(graph, node_count)

    reinitialize()
    dfs(relabeled_graph, node_count)


def main(argv):
    graph, reversed_graph, vertices = construct_graphs(argv[0])

    node_count = len(vertices)
    sys.setrecursionlimit(1048576)

    scc(graph, reversed_graph, node_count)

    stats = sorted([len(values) for values in components.values()], reverse = True)

    print
    print 'Top 5 SCCs: %s' % str(stats[0:5])
    print


if __name__ == "__main__":
    main(sys.argv[1:])
