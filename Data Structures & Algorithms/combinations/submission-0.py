class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(i, comb, num):
            if num == k:
                res.append(comb.copy())
                return

            if i > n:
                return 

            comb.append(i)
            dfs(i+1, comb, num+1)
            comb.pop()
            dfs(i+1, comb, num)




        dfs(1, [], 0)
        return res