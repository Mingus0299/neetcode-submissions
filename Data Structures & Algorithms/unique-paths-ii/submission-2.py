class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dp = [0] * (COLS+1)
        dp[COLS-1] = 1

        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS-1, -1, -1):
                if grid[r][c]:
                    dp[c] = 0
                else:
                    dp[c] += dp[c+1]

        return dp[0]