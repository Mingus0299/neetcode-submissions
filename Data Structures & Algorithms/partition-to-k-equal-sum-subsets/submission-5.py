class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False

        target = sum(nums) // k

        subsets = [0] * k
        nums.sort(reverse = True)

        def backtrack(i):
            if i == len(nums):
                return True

            for j in range(k):
                if nums[i] + subsets[j] <= target:
                    subsets[j] += nums[i]
                    if backtrack(i+1):
                        return True
                    subsets[j] -= nums[i]

                if subsets[j] == 0:
                    break
            return False
        
        return backtrack(0)