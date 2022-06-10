"""
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.
Example 1:

Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Example 2:

Input: head = [1,1,1,2,3]
Output: [2,3]
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = {}
        new_head = ListNode()
        node = new_head

        while head != None:
            seen[head.val] = True
            if head.next and head.next.val in seen.keys():
                while head.next and head.next.val in seen:
                    head = head.next
            else:
                node.next = ListNode(val = head.val)
                node = node.next

            head = head.next

        return new_head.next

def createLinkedList(input_arr):
    if len(input_arr) < 1:
        return None
    first_node = ListNode(input_arr[0])
    other_node = first_node
    for k, v in enumerate(input_arr[1:]):
        other_node.next = ListNode(v)
        other_node = other_node.next

    return first_node
from typing import List
def convertFromLinkedList(head: Optional[ListNode]) -> List[str]:
    if not head:
        return []
    output = [head.val]
    while head.next != None:
        head = head.next
        output.append(head.val)

    return output

x = Solution()
testcase = [1,2,3,3,4,4,5]

print(convertFromLinkedList(x.deleteDuplicates(createLinkedList(testcase))))