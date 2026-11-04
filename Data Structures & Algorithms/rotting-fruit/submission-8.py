class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        fresh = 0
        q = deque()
        steps = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh+=1

                if grid[r][c] == 2:
                    q.append([r,c])

        while q and fresh > 0:
            steps+=1
            q_len = len(q)
            for i in range(q_len):
                r,c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or grid[nr][nc]!=1:
                        continue
                    fresh-=1
                    grid[nr][nc] = 2
                    q.append([nr,nc])

        return steps if fresh==0 else -1
