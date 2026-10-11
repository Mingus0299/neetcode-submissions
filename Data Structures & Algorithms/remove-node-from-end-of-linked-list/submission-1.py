# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:


# 1, 2, 3, 4, 5        2
#       3 ->  5


        right = head
        for i in range(n):
            right = right.next

        if not right:
            return head.next

        left = head

        while(right and right.next):
            left = left.next
            right = right.next

        left.next = left.next.next

        return head

        