class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        def dfs(cur, i):
            if sum(cur) == target:
                res.append(cur.copy())
                return

            if sum(cur) > target or i >= len(nums):
                return

            cur.append(nums[i])
            dfs(cur, i)

            cur.pop()
            dfs(cur, i+1)

        dfs([], 0)
        return res