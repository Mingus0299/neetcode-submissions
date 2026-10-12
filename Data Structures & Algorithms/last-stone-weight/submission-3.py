class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while(len(stones) > 1):
            n1 = heapq.heappop(stones)
            n2 = heapq.heappop(stones)

            if n2 > n1:
                heapq.heappush(stones, n1-n2)

        stones.append(0)
        return abs(stones[0])
        