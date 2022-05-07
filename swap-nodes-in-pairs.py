"""
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
"""
from typing import Optional, List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        # First item is the only edge case where there is nothing pointed to it
        # It seems to be useful to use a "dummy" node?
        node = head
        new_head = head.next
        # swap_left, swap_right, outside_swap
        # outside_swap.next = swap_right
        # swap_left.next = swap_right.next
        # swap_right.next = swap_left
        nodes_passed = 0
        prev_node = None
        while node and node.next != None:
            if nodes_passed % 2 == 0:
                swap_left = node
                swap_right = swap_left.next
                outside_swap = prev_node
                
                # Do all the swapping stuff
                if outside_swap:
                    outside_swap.next = swap_right
                swap_left.next = swap_right.next
                swap_right.next = swap_left
                
                node = swap_left # Seems unnecessary?
                nodes_passed += 1

            
            prev_node = node
            node = node.next
            nodes_passed += 1
        return new_head



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
       [1,2,3,4],
       [1,2],
       [1,2,3],
       [],
       [1]
    ]
    correct_answers = [
        [2,1,4,3],
        [2,1],
        [2,1,3],
        [],
        [1],
    ]
    x = Solution()
    for i, t in enumerate(test_cases):
        my_ll_head = createLinkedList(t)
        my_answer = convertFromLinkedList(x.swapPairs(my_ll_head))
        print(
            f"{'Correct' if my_answer == correct_answers[i] else 'Wrong'} : {my_answer} ({correct_answers[i]})"
        )
