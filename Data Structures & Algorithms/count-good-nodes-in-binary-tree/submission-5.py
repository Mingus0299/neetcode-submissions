# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(maxval, node):
            if not node:
                return 0

            res = 0
            if node.val >= maxval:
                res = 1

            maxval = max(maxval, node.val)
            res += dfs(maxval, node.left)
            res += dfs(maxval, node.right)
            return res
        
        return dfs(-101, root)