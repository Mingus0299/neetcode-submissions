class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        res = float("inf")

        while l <= r:
            mid = (l + r) // 2

            i = 0
            total = 0
            time = 0
            while i < len(weights):
                total+=weights[i]
                if total > mid:
                    time+=1
                    total = weights[i]
                i+=1
            time+=1

            if time <= days:
                res = mid 
                r = mid - 1

            else:l = mid +1

        return res

