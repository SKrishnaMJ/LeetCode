# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d = ListNode()
        cur = d
        slow = fast = head
        while fast and fast.next:
            cur.next=slow
            cur=slow
            slow = slow.next
            fast = fast.next.next
        cur.next = slow.next
        return d.next
        
        