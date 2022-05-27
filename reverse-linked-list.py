"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return
        def switchDirection(this_node: ListNode, prev_node: ListNode) -> None:
            tmp = this_node.next
            this_node.next = prev_node
            if tmp == None:
                return this_node
            else:
                return switchDirection(tmp, this_node)

        return switchDirection(head, None)
