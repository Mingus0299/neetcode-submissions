class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, t in enumerate(tasks):
            t.append(i)

        tasks.sort(key = lambda t: t[0])
        minH = []# process time, index
        q = deque() # iddle task
        i = 0
        time = tasks[i][0]
        res = []

        while i < len(tasks) or minH:
            while i < len(tasks) and tasks[i][0] <= time:
                heapq.heappush(minH, [tasks[i][1], tasks[i][2]])
                i+=1
            if minH:
                process, idx = heapq.heappop(minH)
                time += process
                res.append(idx)
            else:
                time = tasks[i][0]

        return res


        