import sys

N = 0

explored   = {}
leaders    = {}
finishing  = {}
statistics = {}


def scc(file_path, node_count):
    global N

    N = node_count
    sys.setrecursionlimit(node_count)

    graph, reversed_graph = construct_graphs(file_path)

    initialize()
    dfs_loop(reversed_graph)

    relabeled_graph = relabel_graph(graph)

    initialize()
    dfs_loop(relabeled_graph)

    return statistics


def construct_graphs(file_path):
    graph          = {}
    reversed_graph = {}

    for i in range(1, N + 1):
        graph[i]          = []
        reversed_graph[i] = []

    with open(file_path) as file:
        for line in file:
            split = line.split()
            tail  = int(split[0])
            head  = int(split[1])
            graph[tail].append(head)
            reversed_graph[head].append(tail)

    return graph, reversed_graph


def initialize():
    for node in range(1, N + 1):
        explored[node]   = False
        leaders[node]    = 0
        finishing[node]  = 0
        statistics[node] = 0


def dfs_loop(graph):
    global t
    global s

    t = 0
    s = 0
    for node in reversed(range(1, N + 1)):
        if not explored[node]:
            s = node
            dfs(graph, node)


def dfs(graph, vertex):
    global t

    explored[vertex] = True
    leaders[vertex]  = s
    statistics[s] += 1
    for node in graph[vertex]:
        if not explored[node]:
            dfs(graph, node)
    t = t + 1
    finishing[vertex] = t


def relabel_graph(graph):
    relabeled_graph = {}
    for node in range(1, N + 1):
        relabeled_heads = []
        for head in graph[node]: 
            relabeled_heads.append(finishing[head])
        relabeled_graph[finishing[node]] = relabeled_heads
    return relabeled_graph


def main(argv):
    stats = scc(argv[0], 875714)

    sorted_stats = sorted(stats.values())
    sorted_stats.reverse()

    print 'top 5 sccs: %s' % str(sorted_stats[0:5])


if __name__ == "__main__":
    main(sys.argv[1:])
