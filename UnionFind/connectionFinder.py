class connectionFinder:
    def __init__(self, length):
        self.id = [0] * length
        self.size = [0] * length

        for i in range(length):
            self.id[i] = i
            self.size[i] = i

    # Id2 will become a root of Id1 :

    def union(self, id1, id2):
        rootA = self.find(id1)
        rootB = self.find(id2)
        self.id[rootA] = rootB
        print(self.id)

    def find(self, x):

        if self.id[x] == x:
            return x
        x = self.id[self.id[x]]
        # To cut the overhead next when we call this find method for the same root
        self.id[x] = x
        return self.find(x)

    def isConnected(self, id1, id2):
        return self.find(id1) == self.find(id2)


uf = connectionFinder(10)
uf.union(1, 2)
print(" check ", uf.isConnected(1, 2))
