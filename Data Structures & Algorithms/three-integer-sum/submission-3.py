class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        ans = []
        nums.sort()

        i = 0
        # sort nums
        
        while (i < (len(nums))):

            if (nums[i] > 0):
                break

            j = i+1
            k = len(nums) - 1

            while (j < k):
                sums = nums[i] + nums[j] + nums[k]
                if sums < 0:
                    j+=1

                elif sums > 0:
                    k-=1

                else:
                    ans.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1

                    while nums[j] == nums[j - 1] and j < k:
                        j += 1

            i +=1
            while(i < (len(nums)) and nums[i] == nums[i-1]):
                i+=1

            
        return ans
