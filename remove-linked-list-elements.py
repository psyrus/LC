"""
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional, List
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None

        dummy = ListNode()
        node = dummy

        while head:
            node.next = None
            if head.val == val:
                head = head.next
                continue
            node.next = head
            node = node.next

            head = head.next
        return dummy.next


def createLinkedList(input_arr):
    if len(input_arr) < 1:
        return None
    first_node = ListNode(input_arr[0])
    other_node = first_node
    for k, v in enumerate(input_arr[1:]):
        other_node.next = ListNode(v)
        other_node = other_node.next

    return first_node

def convertFromLinkedList(head: Optional[ListNode]) -> List[str]:
    if not head:
        return []
    output = [head.val]
    while head.next != None:
        head = head.next
        output.append(head.val)

    return output

if __name__ == '__main__':
    test_cases = [
       ([1,2,6,3,4,5,6], 6)
    ]
    correct_answers = [
        [1,2,3,4,5]
    ]
    x = Solution()
    for i, t in enumerate(test_cases):
        my_ll_head = createLinkedList(t[0])
        my_answer = convertFromLinkedList(x.removeElements(my_ll_head, t[1]))
        print(
            f"{'Correct' if my_answer == correct_answers[i] else 'Wrong'} : {my_answer} ({correct_answers[i]})"
        )
