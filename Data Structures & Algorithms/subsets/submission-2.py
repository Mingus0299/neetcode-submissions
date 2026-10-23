class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
# backtracking      
# res -> final list of all subsets
# subset -> current subset been built

# define recursive function dfs(i)
#     case case: if i >= len(nums): append current subset to res and return


#   add current number to subset then run dfs on it with same i
#   remove the number from subset (backtrack) then run dfs on it with i + 1 so recur se ot next index


        res = []

        def dfs(i, subset):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i+1, subset)
            subset.pop()
            dfs(i+1, subset)

        dfs(0, [])

        return res


