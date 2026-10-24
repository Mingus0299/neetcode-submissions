class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target = sum(nums) // k

        if sum(nums) % k != 0:
            return False

        subset = [0] * k
        nums.sort(reverse = True)

        def backtracking(i):
            if i == len(nums):
                return True

            for j in range(k):
                if nums[i] + subset[j] <= target:
                    subset[j] += nums[i]
                    if backtracking(i+1):
                        return True
                    subset[j] -= nums[i]
                if subset[j] == 0:
                    break

            return False
        return backtracking(0)
        