class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1

        maxw = 0

        while (l < r):
            area = min(heights[l], heights[r]) * (r-l)

            maxw = max(maxw, area)

            if (heights[l] < heights[r]):
                l+=1

            else:
                r-=1

        return maxw