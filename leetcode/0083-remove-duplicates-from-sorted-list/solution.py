# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        r = ListNode()
        res = r
        l = []

        while head:
            if head.val not in l:
                l.append(head.val)
            head = head.next
        
        for i in l:
            r.next = ListNode(i)
            r = r.next
        
        return res.next


