class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])

        if obstacleGrid[ROWS-1][COLS-1] == 1:
            return 0

        grid = [[0] * COLS for _ in range(ROWS)]

        grid[ROWS-1][COLS-1] = 1

        for r in range(ROWS-1, -1, -1):
            for c in range(COLS-1, -1, -1):

                if obstacleGrid[r][c] == 1:
                    grid[r][c] = 0

                else:
                    grid[r][c] += grid[r][c+1] if c != COLS-1 else 0
                    grid[r][c] += grid[r+1][c] if r != ROWS-1 else 0

        return grid[0][0]