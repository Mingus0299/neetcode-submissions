class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        lst = [-s for s in stones]

        heapq.heapify(lst)

        while len(lst) >= 2:
            stone1, stone2 = heapq.heappop(lst), heapq.heappop(lst)

            if stone1 < stone2:
                stone1 = stone1 - stone2
                heapq.heappush(lst, stone1)

            elif stone1 > stone2:
                stone2 = stone2 - stone1
                heapq.heappush(lst, stone2)

        return -lst[0] if lst else 0