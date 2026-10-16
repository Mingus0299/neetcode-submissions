class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # a tree has n edges, n+1 nodes
        # in our case n edges, n nodes
        par = [i for i in range(len(edges)+1)]
        rank = [1] * (len(edges)+1)

        def find(n1):
            res = n1
            while par[res]!=res:
                par[res] = par[par[res]]
                res = par[res]

            return res

        



        for n1, n2 in edges:
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return [n1,n2]

            if p1 > p2:
                par[p2] = p1
                rank[p1] += rank[p2]

            else:
                par[p1] = p2
                rank[p2] += rank[p1]