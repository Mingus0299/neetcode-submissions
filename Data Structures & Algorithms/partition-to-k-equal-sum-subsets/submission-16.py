class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False

        target = sum(nums) // k

        subset = []
        pick = [False] * len(nums)

        def backtrack(i, k, sumsubset):
            if k == 0:
                return True
            
            if sumsubset == target:
                return backtrack(0, k-1, 0)

            for j in range(i, len(nums)):
                if not pick[j] and sumsubset + nums[j] <= target:
                    pick[j] = True
                    if backtrack(j+1, k , sumsubset + nums[j]):
                        return True
                    pick[j] = False

            return False

        return backtrack(0, k, 0)
