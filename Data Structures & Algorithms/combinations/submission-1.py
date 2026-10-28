class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def dfs(comb, i):
            if len(comb) == k:
                res.append(comb.copy())
                return

            elif i > n:
                return

            comb.append(i)
            dfs(comb, i+1)
            comb.pop()
            dfs(comb, i+1)

        dfs([], 1)
        return res