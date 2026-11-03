class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        count = {"a" : a, "b":b, "c":c}
        maxH = []
        for char, cnt in count.items():
            if cnt:
                heapq.heappush(maxH, [-cnt, char])

        res = ""
        while maxH:
            cnt, char = heapq.heappop(maxH)
            if len(res)>1 and char == res[-1] == res[-2]:
                if not maxH:
                    break
                cnt2, char2 = heapq.heappop(maxH)
                heapq.heappush(maxH, [cnt, char])
                cnt, char = cnt2, char2

            res+=char
            cnt+=1
            if cnt:
                heapq.heappush(maxH, [cnt, char])
        
        return res
        