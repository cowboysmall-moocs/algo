import sys

N = 875714

explored  = {}
leaders   = {}
finishing = {}
stats     = {}


def initialize():
    for node in range(1, N + 1):
        explored[node]  = False
        leaders[node]   = 0
        finishing[node] = 0
        stats[node]     = 0


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
    stats[s] += 1
    for node in graph[vertex]:
        if not explored[node]:
            dfs(graph, node)
    t = t + 1
    finishing[vertex] = t


def relabel_graph(graph):
    relabeled = {}
    for node in range(1, N + 1):
        temp = []
        for x in graph[node]: 
            temp.append(finishing[x])
        relabeled[finishing[node]] = temp
    return relabeled


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

    new_graph = relabel_graph(graph)

    initialize()
    dfs_loop(new_graph)

    sorted_stats = sorted(stats.values())
    sorted_stats.reverse()

    print '[%s]' % str(sorted_stats[0:5]).strip('[]')



if __name__ == "__main__":
    main(sys.argv[1:])
