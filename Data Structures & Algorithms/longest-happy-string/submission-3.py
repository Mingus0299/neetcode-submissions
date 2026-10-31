class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxH = []

        for count, char in [[-a, "a"], [-b, "b"], [-c, "c"]]:
            if count!=0:
                heapq.heappush(maxH, [count, char])
        res = ""

        while maxH:
            cnt, char = heapq.heappop(maxH)
            if len(res) > 1 and char == res[-1] == res[-2]:
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




