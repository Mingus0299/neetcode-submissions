class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, t in enumerate(tasks):
            t.append(i)

        tasks.sort(key = lambda t: t[0])

        i = 0
        time = tasks[0][0]
        minH = []
        heapq.heapify(minH)
        res = []

        while minH or i < len(tasks):
            while i < len(tasks) and tasks[i][0] <= time:
                heapq.heappush(minH, [tasks[i][1], tasks[i][2]])
                i+=1

            if minH:
                process, index = heapq.heappop(minH)
                res.append(index)
                time += process

            else:
                time = tasks[i][0]
        return res