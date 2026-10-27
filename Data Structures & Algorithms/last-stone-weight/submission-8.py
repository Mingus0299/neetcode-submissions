class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        lst = [-s for s in stones]

        heapq.heapify(lst)

        while len(lst) >=2:
            stone1 = heapq.heappop(lst)
            stone2 = heapq.heappop(lst)

            if stone1 > stone2:
                heapq.heappush(lst, stone2-stone1)
            elif stone2 > stone1:
                heapq.heappush(lst, stone1-stone2)

        return -(lst[0]) if lst else 0