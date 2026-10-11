"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        cur = head
        while cur:
            l2 = Node(cur.val)
            l2.next = cur.next
            cur.next = l2
            cur = l2.next

        cur = head
        while cur:
            temp = cur
            if cur.random is not None:
                cur.next.random = cur.random.next
            cur = cur.next.next

        ans = head.next

        cur = head
        while cur:
            l2 = cur.next
            cur.next = l2.next
            if l2.next is not None:
                l2.next = cur.next.next
            cur = cur.next

        return ans



        