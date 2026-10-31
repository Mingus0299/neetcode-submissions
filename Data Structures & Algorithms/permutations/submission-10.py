class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        pick = [False] * len(nums)
        res = []


        def dfs(pick, subset):
            if len(subset) == len(nums):
                res.append(subset.copy())
                return
            
            for i in range(len(nums)):
                if not pick[i]:
                    subset.append(nums[i])
                    pick[i] = True
                    dfs(pick, subset)
                    subset.pop()
                    pick[i] = False


        dfs(pick, [])
        return res