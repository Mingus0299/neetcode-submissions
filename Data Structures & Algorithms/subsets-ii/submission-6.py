class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()

        def dfs(i, subset):
            if i >= len(nums):
                res.add(tuple(subset))
                return

            subset.append(nums[i])
            dfs(i+1, subset)
            subset.pop()
            dfs(i+1, subset)

        dfs(0, [])
        return [list(s) for s in res]

        