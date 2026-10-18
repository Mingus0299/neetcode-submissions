class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(cur, i):

            if i == len(nums):
                res.append(cur.copy())
                return

            cur.append(nums[i])
            dfs(cur, i+1)
            cur.pop()
            dfs(cur, i+1)
        
        dfs([], 0)
        return res