class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cur, keep = 0, 0 

        while cur < len(nums):
            if nums[cur]!= val:
                nums[keep] = nums[cur]
                keep+=1
            cur+=1

        k = keep
        return k