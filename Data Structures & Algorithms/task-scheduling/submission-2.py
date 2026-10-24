class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        count = Counter(tasks) # char: count

        maxH = []

        for char, cnt in count.items():
            maxH.append([-cnt,char])

        queue = deque()
        time = 0

        heapq.heapify(maxH)

        while maxH or queue:
            if maxH:
                time+=1

                cnt, char = heapq.heappop(maxH)
                cnt+=1

                if cnt:
                    queue.append([time+n, cnt, char])


                if queue and queue[0][0] == time:
                        time, cnt, char = queue.popleft()
                        heapq.heappush(maxH, [cnt, char])

            else:
                
                time, cnt, char = queue.popleft()
                heapq.heappush(maxH, [cnt, char])

            

            
        return time

