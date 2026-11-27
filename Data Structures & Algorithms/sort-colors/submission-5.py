class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        cur = 0
        left = 0
        right = len(nums) - 1

        def swap(l, r):
            temp = nums[r]
            nums[r] = nums[l]
            nums[l] = temp

        while cur <= right:
            if nums[cur] == 0:
                swap(cur, left)
                left+=1
                cur+=1

            elif nums[cur] == 2:
                swap(cur, right)
                right-=1

            else:
                cur+=1

        

        