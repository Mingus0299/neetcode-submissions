class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and nums[i] == nums[i-1]:
                continue

            j = i+1
            k = len(nums)-1

            while (j < k):
                three = nums[i] + nums[j] + nums[k]

                if three > 0:
                    k-=1

                elif three < 0:
                    j+=1
                
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    k-=1
                    j+=1
                    while(nums[j] == nums[j-1] and j < k):
                        j+=1

        return res