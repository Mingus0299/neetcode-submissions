class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        res = [[] for i in range (len(nums)+1)]

        for num in nums:
            mp[num] = mp.get(num, 0)+1

        for num, freq in mp.items():
            res[freq].append(num)

        answer = []
        for i in range(len(res)-1, -1, -1):
            for n in res[i]:
                answer.append(n)
                if len(answer) == k:
                    return answer

        
        
        
