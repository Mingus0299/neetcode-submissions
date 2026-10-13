class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtracking(i, cur, total):
            if i == len(nums) or total > target:
                return
            if total == target:
                ans.append(cur.copy())
                return


            total+=nums[i]
            cur.append(nums[i])
            backtracking(i, cur, total)
            cur.pop()
            total-=nums[i]
            backtracking(i+1, cur, total)

        backtracking(0, [], 0)

        return ans

