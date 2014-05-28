import sys


class DFS:

    def __init__(self, directed_graph_dict):
        self.directed_graph_dict = directed_graph_dict


    def dfs(self):
        self.dfs_node_count = len(self.directed_graph_dict)
        self.dfs_explored   = {}
        self.dfs_ordering   = []

        for vertex in self.directed_graph_dict.keys():
            if vertex not in self.dfs_explored or not self.dfs_explored[vertex]:
                self._dfs_recursive(vertex)

        self.dfs_ordering.reverse()
        return self.dfs_ordering


    def _dfs_recursive(self, vertex):
        self.dfs_explored[vertex] = True
        for v in self.directed_graph_dict[vertex]:
            if v not in self.dfs_explored or not self.dfs_explored[v]:
                self._dfs_recursive(v)

        self.dfs_ordering.append(vertex)




class SCC:

    def __init__(self, directed_graph_dict, ordering):
        self.directed_graph_dict = directed_graph_dict
        self.sccs                = {}
        self.ordering            = ordering
        self.dfs_explored        = {}
        self.count               = 0

    def scc(self):
        for vertex in self.ordering:
            if vertex not in self.dfs_explored or not self.dfs_explored[vertex]:
                self._dfs_recursive(vertex)
                self.count += 1

    def _dfs_recursive(self, vertex):
        self.dfs_explored[vertex] = True

        if self.count not in self.sccs:
            self.sccs[self.count] = []

        self.sccs[self.count].append(vertex)

        for v in self.directed_graph_dict[vertex]:
            if v not in self.dfs_explored or not self.dfs_explored[v]:
                self._dfs_recursive(v)

    def sccs(self):
        return self.sccs

    def count(self):
        return self.count



def main(argv):
    file = open(argv[0])
    edge_list = [element.strip('\r\n').split(' ') for element in file.readlines()]
    file.close()

    directed_graph_dict = {}
    reversed_directed_graph_dict = {}
    for row in edge_list:
        tail = long(row[0])
        head = long(row[1])

        if tail not in directed_graph_dict:
            directed_graph_dict[tail] = []
        directed_graph_dict[tail].append(head)

        if head not in reversed_directed_graph_dict:
            reversed_directed_graph_dict[head] = []
        reversed_directed_graph_dict[head].append(tail)

    sccs = SCC(directed_graph_dict, DFS(reversed_directed_graph_dict).dfs()).sccs()
    print 'count of sccs -> ', len(sccs)
    for scc in sccs:
        print '          scc -> ', scc




if __name__ == "__main__":
    main(sys.argv[1:])
