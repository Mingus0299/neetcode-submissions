class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minH = [-s for s in stones]
        heapq.heapify(minH)

        while len(minH) > 1:
            stone1, stone2 = heapq.heappop(minH), heapq.heappop(minH)

            diff = abs(stone1 - stone2)

            if diff > 0:
                heapq.heappush(minH, -diff)

        return (-minH[0]) if minH else 0