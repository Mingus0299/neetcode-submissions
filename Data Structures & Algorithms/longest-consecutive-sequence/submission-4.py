class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0

        for n in numSet:
            if n-1 not in numSet:
                length = 0
                while n in numSet:
                    n+=1
                    length+=1
                res = max(length, res)

        return res