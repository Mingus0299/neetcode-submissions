class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.sumatrix = [[0] * (COLS+1) for i in range(ROWS + 1)]

        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                prefix+=matrix[r][c]
                above = self.sumatrix[r][c+1]
                self.sumatrix[r+1][c+1] = prefix + above


        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:



        big_rectangle = self.sumatrix[row2+1][col2+1]
        left_rectangle = self.sumatrix[row2+1][col1]
        above_rectangle = self.sumatrix[row1][col2+1]
        small_rectangle = self.sumatrix[row1][col1]
        total = big_rectangle - left_rectangle - above_rectangle + small_rectangle

        return total



        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)