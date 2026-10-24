class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = defaultdict(int)
        mp[0] = 1

        cur=0
        res = 0

        for num in nums:
            cur+=num
            diff = cur - k

            if diff in mp:
                res+= mp[diff]
            
            mp[cur]+=1

        return res
