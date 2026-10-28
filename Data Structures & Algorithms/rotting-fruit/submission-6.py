class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        fresh = 0
        q = deque()
        time = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh+=1
                if grid[r][c] == 2:
                    q.append([r,c])

        while q and fresh > 0:
            q_len = len(q)
            for i in range(q_len):
                row, col = q.popleft()

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2
                    fresh-=1
                    q.append([nr,nc])

            time +=1

        return time if fresh == 0 else -1