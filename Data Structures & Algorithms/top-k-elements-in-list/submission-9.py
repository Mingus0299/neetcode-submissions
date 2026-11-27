class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        mp = {}
        freqs = [[] for i in range(len(nums) + 1)]

        for n in nums:
            mp[n] = mp.get(n,0)+1

        for num, freq in mp.items():
            freqs[freq].append(num)

        i = len(nums)
        res = []

        while i > 0 and k > 0:
            for n in freqs[i]:
                res.append(n)
                k-=1
            i-=1
        return res


        
        