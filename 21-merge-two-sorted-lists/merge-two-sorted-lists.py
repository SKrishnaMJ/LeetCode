# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        d = ListNode()
        temp = d
        cur1 = list1
        cur2 = list2
        while cur1 and cur2:
            if cur1.val <= cur2.val:
                d.next = cur1
                d = cur1
                cur1 = cur1.next
            else:
                d.next = cur2
                d = cur2
                cur2 = cur2.next
        if cur1:
            d.next = cur1
        else:
            d.next = cur2
        return temp.next


        