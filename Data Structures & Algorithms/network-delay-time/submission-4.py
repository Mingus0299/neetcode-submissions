class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for u,v,t in times:
            adj[u].append([t,v])

        
        res = 0

        visit = set()
        minH = [[0, k]]

        while minH:
            time, src = heapq.heappop(minH)
            
            if src in visit:
                continue
            visit.add(src)
            res = time
            

            for t, nei in adj[src]:
                if nei in visit:
                    continue
                heapq.heappush(minH, [time + t, nei])
                    

        return res if len(visit) == n else -1
            
        