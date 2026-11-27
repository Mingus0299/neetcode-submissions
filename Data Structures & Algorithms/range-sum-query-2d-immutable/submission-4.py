class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS = len(matrix)
        COLS = len(matrix[0])
        self.smatrix = [[0] * (COLS + 1) for r in range(ROWS + 1)]

        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                prefix+=matrix[r][c]
                self.smatrix[r+1][c+1] = prefix + self.smatrix[r][c+1]




    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1+=1
        col1+=1
        row2+=1
        col2+=1

        big_rect = self.smatrix[row2][col2]
        left_rect = self.smatrix[row2][col1-1]
        small_rect = self.smatrix[row1-1][col1-1]
        above_rect = self.smatrix[row1-1][col2]

        return (big_rect-left_rect-above_rect+small_rect)

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)