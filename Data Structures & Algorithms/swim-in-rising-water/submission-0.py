class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])

        minH = [[grid[0][0],0,0]] #time, r, c
        elevation = 0
        visit = set()
        visit.add((0,0))
        directions = [[0,1],[1,0],[0,-1],[-1,0]]

        while minH:
            time, r,c = heapq.heappop(minH)

            if r == ROWS-1 and c == COLS-1:
                return time
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or (nr,nc) in visit:
                    continue
                visit.add((nr, nc))
                heapq.heappush(minH, [max(time, grid[nr][nc]), nr, nc])
                
