# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        
        s,f = head,head.next

        while f and f.next and s!=f:
            s=s.next
            f=f.next.next
        
        return f==s
        