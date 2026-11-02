class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:   
        ROWS = len(matrix)
        COLS = len(matrix[0])

        top = 0
        bot = ROWS -1

        while top <= bot:
            mid_row = (bot + top) // 2
            if target < matrix[mid_row][0]:
                bot = mid_row - 1

            elif target > matrix[mid_row][COLS-1]:
                top  = mid_row + 1

            else:
                break

        row = mid_row
        l = 0
        r = COLS-1
        while l <= r:
            m = (l+r)//2
            if target > matrix[row][m]:
                l = m + 1

            elif target < matrix[row][m]:
                r = m - 1
            
            else:
                return True
        
        return False

        