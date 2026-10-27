class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)

        maxH = [[-cnt, char] for char, cnt in count.items()]
        prev = []

        heapq.heapify(maxH)
        res = ""

        while maxH:
            cnt, char = heapq.heappop(maxH)
            cnt+=1
            res += char

            if prev:
                heapq.heappush(maxH, prev.pop())

            if cnt != 0:
                prev.append([cnt, char])

        if prev:
            return ""
        return res
