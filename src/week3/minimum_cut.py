import sys
import copy
import random

from collections import defaultdict


def construct_graph(file_path):
    graph = defaultdict(list)
    with open(file_path) as file:
        for line in file:
            elements = line.split()
            graph[elements[0]].extend(elements[1:])
    return graph


def min_cut(graph):
    while len(graph) > 2:
        v1 = random.choice(graph.keys())
        v2 = random.choice(graph[v1])

        graph[v1].extend(graph[v2])

        for vertex in graph[v2]:
            if v2 in graph[vertex]:
                graph[vertex].remove(v2)
                graph[vertex].append(v1)

        while v1 in graph[v1]:
            graph[v1].remove(v1)
        del graph[v2]

    return min([len(values) for values in graph.values()])


def main(argv):
    graph = construct_graph(argv[0])

    for iteration in range(10):
        results = []
        for count in range(20):
            results.append(min_cut(copy.deepcopy(graph)))

        print
        print 'Iteration:   ', iteration + 1
        print 'Results :    ', results
        print 'Minimum Cut: ', min(results)
        print


if __name__ == "__main__":
    main(sys.argv[1:])
