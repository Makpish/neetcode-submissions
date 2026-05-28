# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # if not list1:
        #     return list2
        # if not list2:
        #     return list1
        
        c1,c2 = list1, list2
        res = ListNode()
        head=res

        while c1 and c2:
            if c1.val<c2.val:
                res.next = c1
                c1=c1.next
            else:
                res.next = c2
                c2=c2.next
            res = res.next
        
        # rem = c1
        # if not rem:
            # rem = c2
        
        # while rem:
        res.next = c1 or c2
            # rem=rem.next
            # res = res.next
        
        return head.next
        