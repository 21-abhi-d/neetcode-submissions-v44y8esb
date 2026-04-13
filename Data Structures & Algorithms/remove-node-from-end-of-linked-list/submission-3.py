# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        count = 0

        while curr:
            curr = curr.next
            count += 1
        
        target = count - n
        if target == 0:
            return head.next

        curr = head
        new_count = 0
        while curr:
            if (new_count + 1) == target:
                curr.next = curr.next.next
                break
            curr = curr.next
            new_count += 1
        
        return head


        