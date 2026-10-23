class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()
        pick = [False] * len(nums)

        def dfs(perm):
            if len(perm) == len(nums):
                res.add(tuple(perm))
                return

            for i in range(len(nums)):
                if not pick[i]:
                    perm.append(nums[i])
                    pick[i] = True
                    dfs(perm)
                    perm.pop()
                    pick[i] = False

        dfs([])
        return [list(p) for p in res]