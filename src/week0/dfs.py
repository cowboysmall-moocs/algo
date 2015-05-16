

class DFS:

    def __init__(self, directed_graph_dict):
        self.directed_graph_dict = directed_graph_dict


    def dfs(self, iterative = True):
        self.dfs_node_count = len(self.directed_graph_dict)
        self.dfs_explored   = {}
        self.dfs_ordering   = []
        self.dfs_stack      = []

        for vertex in self.directed_graph_dict.keys():
            if vertex not in self.dfs_explored:
                if iterative:
                    self._dfs_iterative(vertex)
                else:
                    self._dfs_recursive(vertex)
        return self.dfs_ordering


    def _dfs_iterative(self, vertex):
        self.dfs_stack = [vertex]

        while self.dfs_stack:
            current = self.dfs_stack.pop()
            if current not in self.dfs_explored:
                self.dfs_explored[current] = True
                if current in self.directed_graph_dict:
                    self.dfs_stack += reversed(self.directed_graph_dict[current])
                self.dfs_ordering.append(current)


    def _dfs_recursive(self, vertex):
        self.dfs_explored[vertex] = True
        self.dfs_ordering.append(vertex)

        for current in self.directed_graph_dict[vertex]:
            if current not in self.dfs_explored:
                self._dfs_recursive(current)

