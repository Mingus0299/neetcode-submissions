class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        area = 0
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(r,c,cur):
            q = deque()
            q.append((r,c))
            grid[r][c] = 2
            

            while q:
                row, col = q.popleft()
                cur+=1

                for dr, dc in directions:
                    nr, nc = dr + row, dc + col

                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] != 1:
                        continue
                    
                    grid[nr][nc] = 2
                    q.append((nr, nc))
            
            return cur

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = max(area, bfs(r,c, 0))
        return area

                    