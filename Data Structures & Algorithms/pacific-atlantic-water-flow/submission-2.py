class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac = set()
        atl = set()

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        ROWS, COLS = len(heights), len(heights[0])

        def bfs(r,c, visit):
            q = deque()
            q.append((r,c))
            visit.add((r,c))

            while(q):
                r,c = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c

                    if((nr,nc) in visit or nr < 0 or nc < 0 or nr >=ROWS or nc >=COLS or heights[nr][nc] < heights[r][c]):
                        continue

                    visit.add((nr,nc))
                    q.append((nr,nc))

        res = []


        for r in range(ROWS):
            bfs(r,0, pac)
            bfs(r,COLS-1, atl)

        for c in range(COLS):
            bfs(0, c, pac)
            bfs(ROWS-1,c, atl)
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])

        return res



                    
