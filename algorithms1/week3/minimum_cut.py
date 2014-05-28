import sys
import copy
import random


def min_cut(graph_dict):
    while len(graph_dict) > 2:
        edge1 = random.choice(graph_dict.keys())
        edge2 = random.choice(graph_dict[edge1])

        graph_dict[edge1].extend(graph_dict[edge2])

        for vertex in graph_dict[edge2]:
            for i in range(len(graph_dict[vertex])):
                if graph_dict[vertex][i] == edge2:
                    graph_dict[vertex][i] = edge1

        while edge1 in graph_dict[edge1]:
            graph_dict[edge1].remove(edge1)

        del graph_dict[edge2]

    return len(graph_dict[graph_dict.keys()[0]])


def main(argv):
    file = open(argv[0])
    adjacency_list = [element.strip('\t\r\n').split('\t') for element in file.readlines()]
    file.close()

    graph_dict = {}
    for row in adjacency_list:
        graph_dict[row[0]] = row[1:]

    for iteration in range(10):
        min = min_cut(copy.deepcopy(graph_dict))
        results = []
        results.append(min)
        for count in range(20):
            current = min_cut(copy.deepcopy(graph_dict))
            results.append(current)
            if current < min:
                min = current

        print 'Iteration:   ', iteration + 1
        print 'Results :    ', results
        print 'Minimum Cut: ', min
        print


if __name__ == "__main__":
    main(sys.argv[1:])
