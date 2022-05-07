"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Edge case where we remove the head
        if head.next == None:
            return None
        nodes = [head]
        next_node = head
        while next_node.next is not None:
            next_node = next_node.next
            nodes.append(next_node)

        # Edge case where the target removal is the head node
        if n == len(nodes):
            return nodes[1]

        nodes[(n + 1) * -1].next = nodes[(n - 1) * -1] if n > 1 else None
        return head

def createLinkedList(input_arr):
    if len(input_arr) < 2:
        return "sigh"
    first_node = ListNode(input_arr[0])
    other_node = first_node
    for k, v in enumerate(input_arr[1:]):
        other_node.next = ListNode(v)
        other_node = other_node.next

    return first_node


if __name__ == '__main__':
    test_cases = [
        ([1,2], 2)
        ([1,2,3,4,5], 2),
        ([1], 1),
        ([1,2], 1),
    ]
    correct_answers = [
        [2]
        [1,2,3,5],
        [],
        [1],
    ]
    x = Solution()
    for i, t in enumerate(test_cases):
        my_ll_head = createLinkedList(t[0])
        my_answer = x.removeNthFromEnd(my_ll_head, t[1])
        print(
            f"{'Correct' if my_answer == correct_answers[i] else 'Wrong'} : {my_answer} ({correct_answers[i]})"
        )
