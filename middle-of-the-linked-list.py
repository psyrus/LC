"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
"""

# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        main_ptr = head
        trailing_ptr = head

        trailing_should_increment = True

        while main_ptr.next != None:
            main_ptr = main_ptr.next

            if trailing_should_increment:
                trailing_ptr = trailing_ptr.next

            trailing_should_increment = not trailing_should_increment

        return trailing_ptr