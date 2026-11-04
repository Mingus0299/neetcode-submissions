class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def backtrack(r,c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] != "1":
                return

            grid[r][c] = "0"
            backtrack(r + 1,c)
            backtrack(r,c + 1)
            backtrack(r - 1,c)
            backtrack(r,c - 1)

        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    backtrack(r,c)
                    islands +=1

        return islands


            