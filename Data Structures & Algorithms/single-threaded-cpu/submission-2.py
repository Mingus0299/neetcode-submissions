class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, t in enumerate(tasks):
            t.append(i)

        tasks.sort(key = lambda t: t[0])

        res, minH = [], []
        i, time = 0 , tasks[0][0]

        while minH or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(minH, [tasks[i][1], tasks[i][2]])
                i+=1

            if minH:
                process, index = heapq.heappop(minH)
                time+=process
                res.append(index)

            else:
                time = tasks[i][0]
        return res