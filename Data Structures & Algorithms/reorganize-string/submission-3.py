class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)

        maxH = [[-cnt, char] for char, cnt in count.items()]

        queue = deque()
        heapq.heapify(maxH)

        res = ""

        while maxH:
            cnt, char = heapq.heappop(maxH)
            cnt+=1
            res+=char

            if queue:
                prevchar, prevcnt = queue.popleft()
                heapq.heappush(maxH, [prevcnt, prevchar])

            if cnt!=0:
                queue.append([char, cnt])

        if not maxH and queue:
            return ""

        return res



