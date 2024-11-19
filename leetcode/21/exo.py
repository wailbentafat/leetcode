# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
       if not list1:
           return list2
       if not list2:
           return list1
       list3=ListNode()
       if list1.val<list2.val:
           list3.val=list1.val
           list1=list1.next
       else:
           list3.val=list2.val
           list2=list2.next
       list3.next=self.mergeTwoLists(list1,list2)
       return list3
       

def create_linked_list(values):

    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head):
    """
    Prints a linked list in a readable format.
    """
    values = []
    while head:
        values.append(str(head.val))
        head = head.next
    print(" -> ".join(values) if values else "Empty List")

# Example Usage
if __name__ == "__main__":
    sol = Solution()

    # Create two sorted linked lists
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])

    print("List 1:")
    print_linked_list(list1)
    print("List 2:")
    print_linked_list(list2)

    # Merge the two lists
    merged_list = sol.mergeTwoLists(list1, list2)

    print("Merged List:")
    print_linked_list(merged_list)
