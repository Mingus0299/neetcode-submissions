class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = defaultdict(int)
        mp[0] = 1

        curSum = 0
        res = 0

        for n in nums:
            curSum+=n
            diff = curSum - k
            if diff in mp:
                res+=mp[diff]

            mp[curSum]+=1

        return res

