# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return [True, 0]

            depth_left = dfs(node.left)
            depth_right = dfs(node.right)

            balanced = depth_left[0] and depth_right[0] and abs(depth_left[1]-depth_right[1]) <= 1
            return [balanced, 1 + max(depth_left[1], depth_right[1])]

        return dfs(root)[0]
