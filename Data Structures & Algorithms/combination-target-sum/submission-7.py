class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        comb = []

        def backtracking(i):
            if sum(comb) == target:
                res.append(comb.copy())
                return

            if i == len(nums) or sum(comb) > target:
                return

            comb.append(nums[i])
            backtracking(i)
            comb.pop()
            backtracking(i+1)

        backtracking(0)
        return res
