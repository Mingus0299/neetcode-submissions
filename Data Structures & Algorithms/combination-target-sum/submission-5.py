class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def backtracking(i, combinations):
            if sum(combinations) == target:
                res.append(combinations.copy())
                return
            if i>= len(nums) or sum(combinations) > target:
                return

            combinations.append(nums[i])
            backtracking(i, combinations)
            combinations.pop()
            backtracking(i+1, combinations)

        backtracking(0, [])
        return res