class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x,y in points:
            dist = x**2 + y**2
            heap.append([dist,x,y])

        res = []

        heapq.heapify(heap)
        while(k > 0):
            ls = heapq.heappop(heap)
            res.append([ls[1],ls[2]])
            k-=1

        return res