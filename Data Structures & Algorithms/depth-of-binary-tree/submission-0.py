# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        count = 0
        curr = root
        count1 = 1+ self.maxDepth(curr.left)
        count2 = 1 + self.maxDepth(curr.right)
        count = max(count1, count2)

        return count