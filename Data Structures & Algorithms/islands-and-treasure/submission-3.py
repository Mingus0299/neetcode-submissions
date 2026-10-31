class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [[-1,0],[0,1],[0,-1],[1,0]]

        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r,c])

        while q:
            len_q = len(q)
            for i in range(len_q):
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr+row, dc+col
                    if nr <0 or nc <0 or nr >= ROWS or nc >= COLS or grid[nr][nc]!=INF:
                        continue
                    q.append([nr,nc])
                    grid[nr][nc] = 1 + grid[row][col]

     
        