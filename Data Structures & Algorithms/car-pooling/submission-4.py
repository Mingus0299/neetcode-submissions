class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        curnum = 0

        trips.sort(key = lambda t: t[1])
        minH = [] # destination, number of people

        for t in trips:
            num, start, end = t
            while minH and minH[0][0] <= start:
                curnum-=heapq.heappop(minH)[1]
            curnum+=num
            heapq.heappush(minH, [end, num])
            if curnum > capacity:
                return False
        
        return True

        