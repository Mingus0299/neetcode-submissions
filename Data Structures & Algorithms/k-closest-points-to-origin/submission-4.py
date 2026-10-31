class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]: 

        minH = []

        for i in range(len(points)):
            x,y = points[i]
            dist = x**2 + y**2
            minH.append([dist,x,y])

        heapq.heapify(minH)
        res = []

        while k > 0:
            point = heapq.heappop(minH)
            res.append([point[1], point[2]])
            k-=1

        return res