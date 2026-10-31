class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, t in enumerate(tasks):
            t.append(i)

        tasks.sort(key = lambda t:t[0])
        i = 0
        time = tasks[i][0]
        maxH = []
        res = []

        while i < len(tasks) or maxH:
            while i < len(tasks) and tasks[i][0] <= time:
                heapq.heappush(maxH, [tasks[i][1], tasks[i][2]])
                i+=1

            if maxH:
                process, index = heapq.heappop(maxH)
                time+=process
                res.append(index)

            else:
                time = tasks[i][0]
        
        return res
