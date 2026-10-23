class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        pick = [False] * len(nums)
        res = []


        def dfs(pick, perm):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            for i in range(len(nums)):
                if not pick[i]:
                
                    perm.append(nums[i])
                    pick[i] = True
                    dfs(pick, perm)
                    pick[i] = False
                    perm.pop()

        dfs(pick, [])
        return res

