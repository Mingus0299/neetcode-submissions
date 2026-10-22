class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        

        targets = defaultdict(list)

        for u,v,w in times:
            targets[u].append((w, v)) # time, target

        minH = [(0,k)]

        visit = set()
        time_max = 0

        while(minH):
            time, node = heapq.heappop(minH)
            if node in visit:
                continue
            visit.add(node)
            time_max = time
            

            for w, target in targets[node]:
                if target in visit:
                    continue
                heapq.heappush(minH, (time_max+w, target))
        
        return time_max if len(visit) == n else -1

