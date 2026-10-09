class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bot = len(matrix) - 1

        while(top <= bot):
            mid = (top+bot)//2
            if target > matrix[mid][-1]:
                top = mid+1

            elif target < matrix[mid][0]:
                bot = mid-1

            else:
                break

        if (top > bot):
            return False

        row = mid
        l = 0
        r = len(matrix[0])-1

        while(l<=r):
            m = (l+r)//2
            if target > matrix[row][m]:
                l = m+1

            elif target < matrix[row][m]:
                r = m-1

            else:
                return True
        return False

            