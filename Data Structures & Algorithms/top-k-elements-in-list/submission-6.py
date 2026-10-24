class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = [[] for i in range(len(nums)+1)]
        mp = {}

        for num in nums:
            mp[num] = mp.get(num,0)+1

        for num, freq in mp.items():
            ans[freq].append(num)

        res = []

        
        while k > 0:
            for i in range(len(ans)-1, -1, -1):
                for j in range(len(ans[i])-1, -1 , -1):
                    res.append(ans[i][j])
                    k-=1
                    if k == 0:
                        return res

        return res