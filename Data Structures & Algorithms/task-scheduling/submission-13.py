class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:


        count = Counter(tasks)
        maxH = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxH)

        res = ""
        time = 0
        q = deque()
        while maxH or q:
            if maxH:
                cnt, char = heapq.heappop(maxH)
                res+=char
                cnt+=1
                if cnt:
                    q.append([time+n, cnt, char])
            else:
                time = q[0][0]

            if q and q[0][0] == time:
                t , cnt, char = q.popleft()
                heapq.heappush(maxH, [cnt, char])
            time+=1
        return time


