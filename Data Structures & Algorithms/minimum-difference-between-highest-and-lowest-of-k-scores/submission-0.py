class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        

# sorting + sliding window
# two points, left and right 
# O(n * log(n))

        nums.sort()
        l = 0
        r = k-1
        answer = nums[r] - nums[l]

        while(r < len(nums)):
            curr = nums[r] - nums[l]
            answer = min(answer, curr)
            l+=1
            r+=1

        return answer


