"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""
from typing import Optional, List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # choose first list
        if not list1 and not list2:
            return None
        lists = []
        if list1 and list2:
            if list1.val <= list2.val:
                lists.append(list1)
                lists.append(list2)
            else:
                lists.append(list2)
                lists.append(list1)
        elif not list2:
            lists.append(list1)
            lists.append(list2)
        elif not list1:
            lists.append(list2)
            lists.append(list1)

        head = lists[0]
        node = head
        lists[0] = lists[0].next

        while lists[0] or lists[1]:
            take_from_list = 0 if (not lists[1]) or (lists[0] != None and lists[0].val != None and lists[0].val <= lists[1].val) else 1
            node.next = lists[take_from_list]
            lists[take_from_list] = lists[take_from_list].next
            node = node.next

        return head

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
        ([-10,-9,-9,0,1,8], [-1,9]),
       ([1,2,4], [1,3,4]),
       ([], []),
       ([], [0]),
       ([1,2,4,7], [1,3,4,6]),
    ]
    correct_answers = [
        
[-10,-9,-9,-1,0,1,8,9],
        [1,1,2,3,4,4],
        [],
        [0],
        [1,1,2,3,4,4,6,7],

    ]
    x = Solution()
    for i, t in enumerate(test_cases):
        my_answer = convertFromLinkedList(x.mergeTwoLists(createLinkedList(t[0]), createLinkedList(t[1])))
        print(
            f"{'Correct' if my_answer == correct_answers[i] else 'Wrong'} : {my_answer} ({correct_answers[i]})"
        )
