class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums)-1
        curr = 0

        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        while curr <= r:
            if nums[curr]== 0:
                swap(l, curr)
                l+=1
                curr+=1

            elif nums[curr] == 2:
                swap(r, curr)
                r-=1

            else:
                curr+=1