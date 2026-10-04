class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cur = 0
        walk = 0

        while(walk < len(nums)):
            if nums[walk] > 0:
                nums[cur] = nums[walk]
                cur+=1

            walk+=1

        while(cur < len(nums)):
            nums[cur] = 0
            cur+=1

        

        return nums
        