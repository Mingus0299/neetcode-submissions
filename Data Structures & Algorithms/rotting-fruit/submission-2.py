class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        q = deque()
        step = 0
        fresh = 0
        
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    fresh+=1


        while(q and fresh > 0):

            length = len(q)
            for i in range(length):

                row, col = q.popleft()
                
                for dr, dc in directions:
                    nr, nc = row+dr, col+dc

                    if(nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] != 1):
                        continue
                    
                    q.append((nr,nc))
                    grid[nr][nc] = 2
                    fresh-=1
            step+=1


        return step if fresh == 0 else -1
                




        

        