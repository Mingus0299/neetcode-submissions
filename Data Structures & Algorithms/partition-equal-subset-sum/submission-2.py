class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:
            return False

        target = sum(nums) // 2
        
        dp = set()
        dp.add(0)

        for i in range(len(nums)-1, -1, -1):
            dp_temp = set()
            for t in dp:
                dp_temp.add(t + nums[i])
                dp_temp.add(t)
            dp = dp_temp

        return True if target in dp else False