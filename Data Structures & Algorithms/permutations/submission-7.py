class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        pick = [False] * len(nums)
        res = []


        def dfs(i, pick, perm):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            for i in range(len(nums)):
                if not pick[i]:
                
                    perm.append(nums[i])
                    pick[i] = True
                    dfs(i+1, pick, perm)
                    pick[i] = False
                    perm.pop()

        dfs(0, pick, [])
        return res

