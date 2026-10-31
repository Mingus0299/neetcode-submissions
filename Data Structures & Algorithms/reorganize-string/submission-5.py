class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxH = [[-cnt, char] for char, cnt in count.items()]

        res = ""
        prev = None

        while maxH or prev:
            if prev and not maxH:
                return ""

            cnt, char = heapq.heappop(maxH)
            res+=char
            cnt+=1

            if prev:
                heapq.heappush(maxH, prev)
                prev = None
            
            if cnt:
                prev = [cnt, char]

        return res
