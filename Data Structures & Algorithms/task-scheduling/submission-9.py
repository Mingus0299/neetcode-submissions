class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxH = [[-cnt, task] for task, cnt in count.items()]

        heapq.heapify(maxH)
        time = 0
        queue = deque()
        while maxH or queue:
            if queue and queue[0][0] == time:
                value = queue.popleft()
                heapq.heappush(maxH, [value[1],value[2]])

            if maxH:
                cnt, task = heapq.heappop(maxH)
                cnt+=1

                if cnt!=0:
                    queue.append([time+n+1, cnt, task])

    
            time+=1
        return time 


