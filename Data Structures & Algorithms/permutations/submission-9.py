class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        pick = [False] * len(nums)
        res = []

        def backtrack(pick, perm):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return 

            for i in range(len(nums)):
                if not pick[i]:
                    perm.append(nums[i])
                    pick[i] = True
                    backtrack(pick, perm)
                    pick[i] = False
                    perm.pop()

        backtrack(pick, [])
        return res

            

            