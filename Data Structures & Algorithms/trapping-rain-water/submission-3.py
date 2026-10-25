class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax = height[0]
        rightmax = height[-1]
        

        l = 0
        r = len(height)-1
        res = 0

        while l < r:
            if leftmax < rightmax:
                l+=1
                leftmax = max(leftmax, height[l])
                res+= (leftmax - height[l])

            else:
                r-=1
                rightmax = max(rightmax, height[r])
                res+= (rightmax - height[r])
        
        return res