class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = []

        for i, n in enumerate(nums):
            if n > 0:
                break

            if i > 0 and nums[i] == nums[i-1]:
                continue

            j,k = i+1, len(nums)-1
            
            while(j < k):
                add = nums[i] + nums[j] + nums[k]
                if add < 0:
                    j+=1
                    while(j<k and nums[j] == nums[j-1]):
                        j+=1 

                elif add > 0:
                    k-=1
                    while(j<k and nums[k] == nums[k+1]):
                        k-=1 

                else:
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while(j<k and nums[j] == nums[j-1]):
                        j+=1 


        return res
                



