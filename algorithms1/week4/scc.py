import sys

N = 875714

explored   = {}
leaders    = {}
finishing  = {}
statistics = {}


def relabel_graph(graph):
    relabeled_graph = {}
    for node in range(1, N + 1):
        relabeled_heads = []
        for head in graph[node]: 
            relabeled_heads.append(finishing[head])
        relabeled_graph[finishing[node]] = relabeled_heads
    return relabeled_graph


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


def dfs_loop(graph):
    global t
    global s

    t = 0
    s = 0
    for node in reversed(range(1, N + 1)):
        if not explored[node]:
            s = node
            dfs(graph, node)


def initialize():
    for node in range(1, N + 1):
        explored[node]   = False
        leaders[node]    = 0
        finishing[node]  = 0
        statistics[node] = 0


def construct_graphs(file_path):
    graph          = {}
    reversed_graph = {}

    for i in range(1, N + 1):
        graph[i]          = []
        reversed_graph[i] = []

    file = open(file_path)
    for line in file:
        tail = int(line.split()[0])
        head = int(line.split()[1])
        graph[tail].append(head)
        reversed_graph[head].append(tail)
    file.close()

    return graph, reversed_graph


def main(argv):
    sys.setrecursionlimit(N)

    graph, reversed_graph = construct_graphs(argv[0])

    initialize()
    dfs_loop(reversed_graph)

    relabeled_graph = relabel_graph(graph)

    initialize()
    dfs_loop(relabeled_graph)

    sorted_stats = sorted(statistics.values())
    sorted_stats.reverse()

    print 'top 5 sccs: %s' % str(sorted_stats[0:5])



if __name__ == "__main__":
    main(sys.argv[1:])
