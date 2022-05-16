"""
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.
"""


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

from typing import Optional
class Solution:
    # This is not my work but I don't care about this binary tree stuff right now so skipping and will come back to it
    def connect(self, root: 'Node') -> 'Node':
        curr = root
        while curr and curr.left:
            left = curr.left
            while curr:
                curr.left.next = curr.right
                curr.right.next = curr.next.left if curr.next else None
                curr = curr.next
            curr = left
        return root

    # Broken and does not work
    # def connectRecursive(self, root: Optional[Node]) -> Optional[Node]:

    #     if not root:
    #         return None

    #     def setNext(left_node: Node, right_node: Node = None):

    #         setNext(right_node.right, None)
    #         setNext(right_node.left, right_node.right)
    #         setNext(left_node.right, right_node.left)
    #         setNext(left_node.left, left_node.right)

    #         left_node.next = right_node
    #         right_node.next = None
    #         print(left_node)
    #         print(right_node)

    #     return root
