class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac = set()
        atl = set()

        ROWS = len(heights)
        COLS = len(heights[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(r,c, ocean):
            q = deque()
            q.append((r,c))
            ocean.add((r,c))
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or (nr, nc) in ocean or heights[nr][nc] < heights[row][col]:
                        continue
                    ocean.add((nr,nc))
                    q.append((nr,nc))

        res = []
        
        for r in range(ROWS):
            bfs(r, 0, pac)
            bfs(r, COLS-1, atl)

        for c in range(COLS):
            bfs(0, c, pac)
            bfs(ROWS-1, c, atl)

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in atl and (r,c) in pac:
                    res.append([r,c])

        return res

        