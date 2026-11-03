"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def dfs(r,c,n):
            val = grid[r][c]
            is_same = True

            for i in range(n):
                for j in range(n):
                    if grid[r+i][c+j] != val:
                        is_same = False
                        break

            if is_same:
                return Node(grid[r][c], True)

            n = n // 2
            topleft = dfs(r,c,n)
            topright = dfs(r,c+n,n)
            bottomleft = dfs(r+n,c,n)
            bottomright = dfs(r+n,c+n,n)

            return Node(0, False, topleft, topright, bottomleft, bottomright)

        return dfs(0,0, len(grid))


