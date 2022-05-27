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

        def helper(prev_node: ListNode, this_node: ListNode):
            if not prev_node and not this_node:
                return None
            next_node = this_node.next
            if this_node.next == None:
                this_node.next = prev_node
                return this_node
            else:
                this_node.next = prev_node
                return helper(this_node, next_node)

        return helper(None, head)