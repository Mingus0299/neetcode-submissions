# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        q = deque()
        res = 0
        maxval = -101
        q.append((root, maxval))

        while(q):

            node,maxval = q.popleft()

            if not node:
                continue

            if node.val >= maxval:
                res+=1
            maxval = max(maxval, node.val)
            
            q.append((node.left,maxval))

           
            q.append((node.right,maxval))

        return res

