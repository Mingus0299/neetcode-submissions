# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        visit = []
        stack = []
        visit.append(False)
        stack.append(root)

        while stack:
            node, v = stack.pop(), visit.pop()
            if node:
                if not v:
                    stack.append(node)
                    visit.append(True)
                    stack.append(node.right)
                    visit.append(False)
                    stack.append(node.left)
                    visit.append(False)

                else:
                    res.append(node.val)

        return res