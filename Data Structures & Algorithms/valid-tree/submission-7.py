class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        rank = [1] * (n)
        parent = [i for i in range(n)]
        comp = n

        def find(node):
            cur = node
            while cur != parent[cur]:
                parent[cur] = parent[parent[cur]]
                cur = parent[cur]

            return cur


        def union(n1, n2):
            nonlocal comp
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False

            comp-=1

            if p1 < p2:
                parent[p2] = p1
                rank[p1] += rank[p2]

            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            
            return True

        for u, v in edges:
            if not union(u,v):
                return False
        return comp == 1

