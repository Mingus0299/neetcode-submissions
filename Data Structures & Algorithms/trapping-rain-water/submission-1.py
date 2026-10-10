class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        leftmax = height[l]
        rightmax = height[r]

        ans = 0

        while(l < r):
            if(leftmax < rightmax):
                l+=1
                leftmax = max(leftmax, height[l])
                ans += (leftmax - height[l])

            else:
                r-=1
                rightmax = max(rightmax, height[r])
                ans+= (rightmax - height[r])

        return ans