from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        output_val = {}
        index = 0
        carry = 0
        while True:
            if not l1 and not l2:
                break
            list1_val = l1.val if l1 else 0
            list2_val = l2.val if l2 else 0
            total = list1_val + list2_val
            total += output_val[index] if index in output_val else 0
            carry = 0 if total < 10 else 1
            total = total if total < 10 else total % 10
            output_val[index] = total
            if carry:
                output_val[index + 1] = carry
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            index += 1

        node_root = ListNode(val = output_val[0])
        expansion_nodes = node_root
        for key in sorted(output_val.keys())[1:]:
            new_node = ListNode(output_val[key])
            expansion_nodes.next = new_node
            expansion_nodes = expansion_nodes.next

        return node_root


if __name__ == '__main__':
    x = Solution()
    #init L1
    l1_list = [9,9,9,9,9,9,9]
    l2_list = [9,9,9,9]
    l1_root = ListNode(l1_list[0])
    l1_walk = l1_root
    for v in l1_list[1:]:
        new_node = ListNode(v)
        l1_walk.next = new_node
        l1_walk = l1_walk.next
        
    l2_root = ListNode(l2_list[0])
    l2_walk = l2_root
    for v in l2_list[1:]:
        new_node = ListNode(v)
        l2_walk.next = new_node
        l2_walk = l2_walk.next
    print(x.addTwoNumbers(l1_root, l2_root))