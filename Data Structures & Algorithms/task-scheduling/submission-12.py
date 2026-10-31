class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        count = Counter(tasks)
        maxH = [[-cnt,char] for char, cnt in count.items()]

        q = deque() # time, cnt, char\
        heapq.heapify(maxH)

        while maxH or q:
            if maxH:
                cnt, char = heapq.heappop(maxH)
                cnt+=1
                time+=1
                if cnt:
                    q.append([time + n, cnt, char])

                if q and q[0][0] <= time:
                    task = q.popleft()
                    heapq.heappush(maxH, [task[1], task[2]])

            else:
                t, cnt, char = q.popleft()
                time = t
                heapq.heappush(maxH, [cnt, char])

        

        return time
