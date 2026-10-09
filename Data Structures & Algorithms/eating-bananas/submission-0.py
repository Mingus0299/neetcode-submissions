class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        l = 1
        r = max(piles)
        res = r

        while(l <= r):
            time = 0
            mid = (l+r)//2
            for pile in piles:
                time += math.ceil(float(pile)/mid)

            if (time <= h):
                res = mid
                r = mid-1

            else:
                l = mid+1
        return res