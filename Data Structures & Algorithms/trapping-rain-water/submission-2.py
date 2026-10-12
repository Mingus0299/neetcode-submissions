class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0, len(height) - 1
        leftmax = height[0]
        rightmax = height[-1]
        water = 0

        while l < r:
            if leftmax < rightmax:
                l+=1
                leftmax = max(leftmax, height[l])
                water += (leftmax - height[l])

            else:
                r-=1
                rightmax=max(rightmax, height[r])
                water += (rightmax-height[r])

        return water

