# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        cnt = c  = 0
        while cur.next:
            cnt+=1
            cur = cur.next
        n = (cnt - n)+1
        d = ListNode()
        cur = d
        cur.next = head
        while head or head.next:
            if c==n:
                cur.next = head.next
                break
            else:
                
                cur = head
                
                head = head.next
                cur.next = head
                

                c+=1
        return d.next
