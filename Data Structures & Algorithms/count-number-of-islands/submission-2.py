class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        islands = 0

        def bfs(r,c):
            q = deque()
            grid[r][c] = "0"
            q.append((r,c))

            while q:
                row,col = q.popleft()
                for dr, dc in directions:
                    ndr, ndc = dr+row, dc+col
                    if(ndr < 0 or ndc < 0 or ndr >=ROWS or ndc >=COLS or grid[ndr][ndc] == "0"):
                        continue
                    q.append((ndr,ndc))
                    grid[ndr][ndc] = "0"

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r,c)
                    islands+=1

        return islands