class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)

        maxH = [[-cnt, char] for char, cnt in count.items()]
        prev = []
        res = ""

        while maxH:
            cnt, char = heapq.heappop(maxH)
            res += char
            cnt+=1

            if prev:
                cntp, charp = prev.pop()
                heapq.heappush(maxH, [cntp, charp])

            if cnt:
                prev.append([cnt, char])
        
        if prev:
            return ""
        return res


