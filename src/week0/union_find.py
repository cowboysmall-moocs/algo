

class QuickFind:
    
    def __init__(self, length):
        self.length = length
        self.array  = [i for i in range(length)]

    def __str__(self):
        return " ".join([str(element) for element in self.array])

    def connected(self, p, q):
        return self.array[p] == self.array[q]

    def union(self, p, q):
        pid = self.array[p]
        qid = self.array[q]
        for i in range(self.length):
            if self.array[i] == pid:
                self.array[i] = qid

    def get_array(self):
        return self.array


class QuickUnion:
    
    def __init__(self, length):
        self.length = length
        self.array  = [i for i in range(length)]

    def __str__(self):
        return " ".join([str(element) for element in self.array])

    def _root(self, i):
        while i != self.array[i]:
            i = self.array[i]
        return i

    def connected(self, p, q):
        return self._root(p) == self._root(q)

    def union(self, p, q):
        proot = self._root(p)
        qroot = self._root(q)
        self.array[proot] = qroot

    def get_array(self):
        return self.array


class WeightedQuickUnion:
    
    def __init__(self, length):
        self.length = length
        self.array  = [i for i in range(length)]
        self.sizes  = [1 for _ in range(length)]

    def __str__(self):
        return " ".join([str(element) for element in self.array])

    def _root(self, i):
        while i != self.array[i]:
            i = self.array[i]
        return i

    def connected(self, p, q):
        return self._root(p) == self._root(q)

    def union(self, p, q):
        proot = self._root(p)
        qroot = self._root(q)
        if proot != qroot:
            if self.sizes[proot] < self.sizes[qroot]:
                self.array[proot] = qroot
                self.sizes[qroot] += self.sizes[proot]
            else:
                self.array[qroot] = proot
                self.sizes[proot] += self.sizes[qroot]

    def get_array(self):
        return self.array

    def get_sizes(self):
        return self.sizes

