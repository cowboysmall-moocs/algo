import sys
import heapq


heap      = []
distances = {}


def construct_graph(file_path):
    graph = {}

    with open(file_path) as file:
        for line in file:
            elements    = line.split()
            tail        = int(elements[0])
            graph[tail] = []
            for heads in elements[1:]:
                values = heads.split(',')
                graph[tail].append((int(values[1]), int(values[0])))

    return graph


def dijkstra_search(graph, edge):
    tail = edge[1]

    for weight, head in graph[tail]:
        if distances[head] > distances[tail] + weight:
            distances[head] = distances[tail] + weight
            if (weight, head) in heap:
                heap.remove((weight, head))
                heapq.heapify(heap)
            heapq.heappush(heap, (distances[head], head))


def dijkstra_shortest_paths(start, graph):
    for i in xrange(1, len(graph) + 1):
        distances[i] = 1000000

    distances[start] = 0
    heapq.heappush(heap, (0, start))

    while len(heap) != 0:
        dijkstra_search(graph, heapq.heappop(heap))

    return distances


def main(argv):
    distances = dijkstra_shortest_paths(int(argv[0]), construct_graph(argv[1]))

    print ",".join([str(distances[node]) for node in [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]])


if __name__ == "__main__":
    main(sys.argv[1:])
