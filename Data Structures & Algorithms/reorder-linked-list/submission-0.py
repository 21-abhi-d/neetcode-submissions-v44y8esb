# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find middle of list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse second half of list
        curr = slow
        prev = None
        while curr:
            next_p = curr.next
            curr.next = prev
            prev = curr
            curr = next_p
        
        # Merge both halves
        p1 = head
        p2 = prev
        while p1.next and p2.next:
            p1_next = p1.next
            p2_next = p2.next
            p1.next = p2
            p2.next = p1_next
            p1 = p1_next
            p2 = p2_next
        





