class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False
        
        target = sum(nums) // k

        used = [False] * len(nums)

        def backtrack(i, k, sumSubset):
            if k == 0:
                return True

            if sumSubset == target:
                return backtrack(0, k-1, 0)

            for j in range(i, len(nums)):
                if not used[j] and sumSubset + nums[j] <= target:
                    used[j] = True
                    if backtrack(j+1, k, sumSubset + nums[j]):
                        return True
                    used[j] = False
            return False

        return backtrack(0, k, 0)

                