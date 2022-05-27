"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode()

        # If either or both are empty, return the one that isn't (or just the second one)
        if not list2 or not list1:
            return list1 or list2

        if list1.val < list2.val:
            node = list1
            list1 = list1.next
        else:
            node = list2
            list2 = list2.next

        new_head.next = node
        while list1 and list2:
            if list1.val <= list2.val:
                 node.next = list1
                 list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        if list1:
            node.next = list1
        elif list2:
            node.next = list2

        return new_head.next