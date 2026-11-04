class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(self.max_rob(nums[0:-1]), self.max_rob(nums[1:]), nums[0])




    def max_rob(self, nums):
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2

