
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fisrtpoin=head.next
        seconspoint=head
        i=0
        if head.next==None:
            return None
        while i<n:
            i=i+1
            fisrtpoin=fisrtpoin.next
            seconspoint=seconspoint.next
            if i==n:
                seconspoint.next=fisrtpoin.next
                
                return head
                
        