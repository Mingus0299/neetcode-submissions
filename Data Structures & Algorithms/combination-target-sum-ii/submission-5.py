class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        candidates.sort() # O(nlogn)

        def dfs(i, total, comb):
            if total == target:
                res.append(comb.copy())
                return

            if total > target or i >= len(candidates):
                return

            comb.append(candidates[i])
            dfs(i+1, total + candidates[i], comb)

            comb.pop()
            while(i+1 < len(candidates) and candidates[i] == candidates[i+1]):
                i+=1
            dfs(i+1, total, comb)

        dfs(0, 0, [])
        return res