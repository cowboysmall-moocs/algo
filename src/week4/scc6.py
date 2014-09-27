import sys

from collections import defaultdict


explored   = defaultdict(bool)
identifier = defaultdict(int)
statistics = defaultdict(int)

stack      = []
count      = 0


def construct_graphs(file_path):
    graph     = defaultdict(list)
    graph_rev = defaultdict(list)

    with open(file_path) as file:
        for line in file:
            split = line.split()
            tail  = int(split[0])
            head  = int(split[1])
            graph[tail].append(head)
            graph_rev[head].append(tail)

    return graph, graph_rev


def reinitialize():
    global explored

    explored   = defaultdict(bool)


def dfs(graph, vertex):
    explored[vertex]   = True
    identifier[vertex] = count

    statistics[count] += 1

    for node in graph[vertex]:
        if not explored[node]:
            dfs(graph, node)


def dfs_loop(graph):
    global count

    for node in reversed(stack):
        if not explored[node]:
            dfs(graph, node)
            count += 1


def dfs_order(graph, vertex):
    explored[vertex] = True

    for node in graph[vertex]:
        if not explored[node]:
            dfs_order(graph, node)

    stack.append(vertex)


def dfs_loop_order(graph):
    for node in sorted(graph.keys()):
        if not explored[node]:
            dfs_order(graph, node)


def scc(graph, graph_rev):
    dfs_loop_order(graph_rev)

    reinitialize()
    dfs_loop(graph)


def main(argv):
    sys.setrecursionlimit(1048576)

    graph, graph_rev = construct_graphs(argv[0])
    scc(graph, graph_rev)

    print
    print 'Number of SCCs: %s' % len(statistics)
    print '    Top 5 SCCs: %s' % str(sorted(statistics.values(), reverse = True)[0:5])
    print


if __name__ == "__main__":
    main(sys.argv[1:])
