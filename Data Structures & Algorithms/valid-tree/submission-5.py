class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if n-1 != len(edges):
            return False
        
        adj_list = [[] for i in range(n)]

        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visit = set()

        def dfs(vertex, prev):
            if vertex in visit:
                return False

            visit.add(vertex)
            for nei in adj_list[vertex]:
                if nei == prev:
                    continue
                if not dfs(nei, vertex):
                    return False

            return True

        return dfs(0, -1) and len(visit) == n
            

