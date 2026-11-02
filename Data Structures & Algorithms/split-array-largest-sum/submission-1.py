class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l = max(nums)
        r = sum(nums)
        res = r

        def cansplit(mid):
            total = 0
            subarray = 0
            for n in nums:
                total +=n
                if total > mid:
                    subarray +=1
                    total = n

            return subarray + 1 <= k



        while l <= r:
            mid = l + (r-l)//2

            if cansplit(mid):
                res = mid
                r = mid -1

            else:
                l = mid + 1
        return res