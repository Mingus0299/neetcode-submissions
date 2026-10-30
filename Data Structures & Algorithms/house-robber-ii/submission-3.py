class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_simple(lst):
            rob1, rob2 = 0, 0
            for n in lst:
                temp = max(rob1+n, rob2)
                rob1 = rob2
                rob2 = temp

            return rob2

        return max(nums[0], rob_simple(nums[:-1]), rob_simple(nums[1:]))