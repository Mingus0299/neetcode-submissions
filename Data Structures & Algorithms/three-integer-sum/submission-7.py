class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
            
        res = []

        i = 0
        while i < len(nums)-2:
            if nums[i] > 0:
                break
            
            if i > 0 and nums[i] == nums[i-1]:
                i+=1
                continue

            j = i+1
            k = len(nums)-1

            while j < k:
                sum3 =  nums[i] + nums[j] + nums[k]
                if sum3 > 0:
                    k-=1
                
                elif sum3 < 0:
                    j+=1

                else:
                    res.append([nums[i], nums[j], nums[k]])
                    k-=1
                    j+=1
                    while j < k and nums[j] == nums[j-1] :
                        j+=1
                        

            i+=1
                    
                    
        return res
