class DSU():
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, n1):
        temp = n1

        while temp != self.parent[temp]:
            self.parent[temp] = self.parent[self.parent[temp]]
            temp = self.parent[temp]

        return temp

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return 0

        elif self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]

        else:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]

        return 1
            



class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        count = n

        dsu = DSU(n)
        for n1, n2 in edges:
            count -= dsu.union(n1,n2)

        return count

        