class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = {i:[] for i in range(n)}

        for i in range(n):
            x1,y1 = points[i]
            for j in range(i+1):
                x2,y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        res = 0
        visit = set()
        minH = [[0,0]]

        while len(visit) < n:
            cost, point = heapq.heappop(minH)
            if point in visit:
                continue

            visit.add(point)
            res+= cost

            for neicost, nei in adj[point]:
                if nei not in visit:
                    heapq.heappush(minH, [neicost, nei])

        return res