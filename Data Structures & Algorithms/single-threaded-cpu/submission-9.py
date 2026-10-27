class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        for i in range(len(tasks)):
            tasks[i].append(i)

        tasks.sort(key = lambda t: t[0])

        process = []
        time = 0
        i = 0
        res = []

        while i < len(tasks) or process:
            while i < len(tasks) and tasks[i][0] <= time:
                
                heapq.heappush(process, [tasks[i][1], tasks[i][2]])
                i+=1

            if process:
                processtime, index = heapq.heappop(process)
                time += processtime
                res.append(index)
            else:
                time = tasks[i][0]

        return res


