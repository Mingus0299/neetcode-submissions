class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        res = float("inf")

        while l <= r:
            m = l + (r-l)//2

            i = 0
            total = 0
            time = 0

            while i < len(weights):
                while  i < len(weights) and total + weights[i] <= m:
                    total+=weights[i]
                    i+=1
                time+=1
                total = 0
            
            if time <= days:
                res = min(res, m)
                r = m-1
            else:
                l = m+1

        return res