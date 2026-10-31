class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac = set()
        atl = set()

        ROWS = len(heights)
        COLS = len(heights[0])

        def dfs(r,c, ocean, prevHeight):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in ocean or heights[r][c] < prevHeight:
                return 

            ocean.add((r,c))
            dfs(r+1, c, ocean, heights[r][c])
            dfs(r, c+1, ocean, heights[r][c])
            dfs(r-1, c, ocean, heights[r][c])
            dfs(r, c-1, ocean, heights[r][c])

        
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS-1, atl, heights[r][COLS-1])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS-1, c, atl, heights[ROWS-1][c])

        res = []

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in atl and (r,c) in pac:
                    res.append([r,c])
        return res