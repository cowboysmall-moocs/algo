

class Graph:

    def __init__(self, graph_dict):
        self.graph_dict = graph_dict


    def vertices(self):
        return list(self.graph_dict.keys())


    def edges(self):
        edges = []

        for vertex in self.graph_dict:
            for neighbour in self.graph_dict[vertex]:
                if (neighbour, vertex) not in edges:
                    edges.append((vertex, neighbour))

        return sorted(edges)


    def adjacent_to(self, vertex):
        return self.graph_dict[vertex]

