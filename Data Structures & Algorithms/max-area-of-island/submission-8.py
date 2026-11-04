class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        area = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(r,c):
            q = deque()
            q.append([r,c])
            area = 0
            grid[r][c] = 0


            while q:
                r,c = q.popleft()
                area+=1
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c

                    if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or grid[nr][nc]!=1:
                        continue

                    grid[nr][nc] = 0
                    q.append([nr,nc])

            return area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = max(area, bfs(r,c))

        return area

