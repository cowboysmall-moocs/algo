


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

