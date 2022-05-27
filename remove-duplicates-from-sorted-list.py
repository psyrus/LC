"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set()
        node = head
        while node and node.next != None:
            seen.add(node.val)
            tmp = node
            while tmp.next != None and tmp.next.val in seen:
                tmp = tmp.next

            node.next = tmp.next
            node = node.next

        return head