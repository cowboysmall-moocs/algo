import sys

from collections import defaultdict


explored   = defaultdict(bool)
finishing  = defaultdict(int)
components = defaultdict(list)

time = 0
s    = None



def construct_graphs(file_path):
    graph     = defaultdict(list)
    graph_rev = defaultdict(list)
    vertices  = set()

    with open(file_path) as file:
        for line in file:
            split = line.split()
            tail  = int(split[0])
            head  = int(split[1])
            graph[tail].append(head)
            graph_rev[head].append(tail)
            vertices |= {tail, head}

    return graph, graph_rev, vertices



def reinitialize():
    global explored

    explored = defaultdict(bool)



def dfs_second(graph, vertex):
    global s

    explored[vertex] = True
    components[s].append(vertex)

    for node in graph[vertex]:
        if not explored[node]:
            dfs_second(graph, node)


def dfs_loop_second(graph, vertices):
    global s

    for node in sorted(vertices, reverse = True):
        if not explored[node]:
            s = node
            dfs_second(graph, node)



def dfs_first(graph, vertex):
    global time

    explored[vertex] = True

    for node in graph[vertex]:
        if not explored[node]:
            dfs_first(graph, node)

    time += 1
    finishing[vertex] = time


def dfs_loop_first(graph, vertices):
    for node in sorted(vertices, reverse = True):
        if not explored[node]:
            dfs_first(graph, node)



def relabel_graph(graph):
    graph_rel    = defaultdict(list)
    vertices_rel = set()

    for node in graph:
        vertices_rel.add(finishing[node])
        for head in graph[node]:
            graph_rel[finishing[node]].append(finishing[head])
            vertices_rel.add(finishing[head])

    return graph_rel, vertices_rel



def scc(graph, graph_rev, vertices):
    dfs_loop_first(graph_rev, vertices)

    graph_rel, vertices_rel = relabel_graph(graph)

    reinitialize()
    dfs_loop_second(graph_rel, vertices_rel)



def main(argv):
    sys.setrecursionlimit(1048576)

    graph, graph_rev, vertices = construct_graphs(argv[0])
    scc(graph, graph_rev, vertices)

    stats = sorted([len(values) for values in components.values()], reverse = True)

    print
    print 'Number of SCCs: %s' % len(stats)
    print '    Top 5 SCCs: %s' % str(stats[0:5])
    print



if __name__ == "__main__":
    main(sys.argv[1:])
