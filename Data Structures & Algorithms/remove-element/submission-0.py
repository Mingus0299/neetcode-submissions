class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

# [0,1,2,2,3,4,2]
# [0,1 ]    cur = 2, walk = 2
# [0,1,3]   cur = 2, walk = 4

        cur = walk = 0

        while(walk < len(nums)):
            if nums[walk] == val:
                walk+=1

            else:
                nums[cur] = nums[walk]
                walk+=1
                cur+=1
        k = cur

        return k
                