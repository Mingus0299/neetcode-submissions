class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        i = 0
        while(i < len(nums)-2):

            if nums[i] > 0:
                break

            if i!=0 and nums[i] == nums[i-1]:
                i+=1
                continue

            j = i + 1
            k = len(nums)-1
            while(j < k):
                threesum = nums[i] + nums[j] + nums[k]
                if threesum > 0:
                    k-=1

                elif threesum < 0:
                    j+=1
                else:
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while(nums[j]  == nums[j-1] and j < k):
                        j+=1

            i+=1

        return res
