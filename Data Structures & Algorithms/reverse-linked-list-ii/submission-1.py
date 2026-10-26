# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        #dummy 1 2 3 4 5       ->dummy 1 4 3 2 5
        
        dummy = ListNode(0, head)
        prev = dummy
        cur = head

        for i in range(left - 1):
            prev, cur = cur, cur.next

        length = right - left + 1

        left = prev
        prev = None
        for i in range(length):
            temp = cur.next
            cur.next = prev
            prev, cur = cur, temp

        temp = left.next
        left.next = prev
        temp.next = cur

        return dummy.next

        
