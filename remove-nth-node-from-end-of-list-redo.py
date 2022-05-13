"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

"""

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # Since I know it is the nth one from the end, I just keep two pointers
        # First pointer goes to the end
        # Second pointer trails by "n" nodes
        # Once first is at the end, I just remove the n-next
        new_head_staging = ListNode()

        new_head_staging.next = head
        end_ptr = head
        trail_ptr = new_head_staging
        nodes_passed = 1
        while end_ptr.next != None:
            if nodes_passed > n - 1:
                trail_ptr = trail_ptr.next
            end_ptr = end_ptr.next
            nodes_passed += 1

        trail_ptr.next = trail_ptr.next.next

        return new_head_staging.next
