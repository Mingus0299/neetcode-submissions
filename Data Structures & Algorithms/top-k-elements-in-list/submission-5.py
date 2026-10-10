class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = [[] for i in range(len(nums) +1)]

        mp = {}

        for num in nums:
            mp[num] = mp.get(num, 0)+1

        for num, freq in mp.items():
            ans[freq].append(num)

        final = []

        for i in range(len(ans) - 1, 0, -1):
            for num in ans[i]:
                final.append(num)
                if len(final) == k:
                    return final
