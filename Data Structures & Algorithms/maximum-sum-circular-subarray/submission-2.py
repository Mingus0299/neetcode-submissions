class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globmax, globmin = nums[0], nums[0]
        curmax, curmin = 0,0
        total = 0

        for num in nums:
            curmax = max(curmax+num, num)
            curmin = min(curmin+num, num)
            total+=num
            globmax = max(globmax, curmax)
            globmin = min(globmin, curmin)

        return max(globmax, total-globmin) if globmax  > 0 else globmax