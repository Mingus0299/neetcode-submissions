class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        step = 0
        q = deque()
        fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh+=1

                if grid[r][c] == 2:
                    q.append([r,c])

        while q and fresh > 0:
            q_len  = len(q)
            for i in range(q_len):
                row, col = q.popleft()

                for dr, dc in directions:
                    nr, nc = dr + row, dc + col

                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] != 1:
                        continue
                    q.append([nr,nc])
                    grid[nr][nc] = 2
                    fresh-=1
            step+=1

        return step if fresh == 0 else -1

        