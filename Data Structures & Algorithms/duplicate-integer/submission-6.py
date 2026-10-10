class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ls = set()

        for num in nums:
            if num in ls:
                return True

            ls.add(num)

        return False