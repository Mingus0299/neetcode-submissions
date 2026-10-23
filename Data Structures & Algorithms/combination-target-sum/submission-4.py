class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def dfs(i, total, subset):
            if total == target:
                res.append(subset.copy())
                return
            
            if total > target or i >= len(nums):
                return

            subset.append(nums[i])
            dfs(i, total+ nums[i], subset)

            subset.pop()
            dfs(i+1, total, subset)

        dfs(0, 0, [])
        return res

# result -> result of combinations 
        
# sort nums

# create recursive function dfs(i, total, comb)
#    base case: if total == target then add a copy of current combination to result and return
#    base case: if total > target or i >= len(nums) then return

#    add current nums[i] to combination and run dfs on it to explore further

#     remove it (backtrack)
#     then run dfs on the next i 
#     

# run dfs
# return res




