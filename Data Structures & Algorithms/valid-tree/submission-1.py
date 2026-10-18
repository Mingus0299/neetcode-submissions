class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n-1:
            return False

        visit = set()
        lst = [[] for _ in range(n)]
        for u,v in edges:
            lst[u].append(v)
            lst[v].append(u)

        def dfs(node, prev):
            if node in visit:
                return False

            visit.add(node)

            for nei in lst[node]:
                if nei == prev:
                    continue
                if not dfs(nei, node):
                    return False


            return True

        return dfs(0, -1) and len(visit) == n
