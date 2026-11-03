class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        pick = [False] * len(nums)
        res = []
        perm = []

        def backtracking(perm, pick):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            for j in range(len(nums)):
                if not pick[j]:
                    perm.append(nums[j])
                    pick[j] = True
                    backtracking(perm, pick)
                    perm.pop()
                    pick[j] = False

        backtracking(perm, pick)
        return res