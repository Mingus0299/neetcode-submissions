class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda t: t[1])

        minH = [] # end, numPass
        currPass = 0

        for t in trips:
            numPass, start, end = t

            while minH and minH[0][0] <= start:
                e, numP = heapq.heappop(minH)
                currPass-=numP

            currPass+=numPass
            if currPass > capacity:
                return False
            
            heapq.heappush(minH, [end, numPass])

        return True
        
            