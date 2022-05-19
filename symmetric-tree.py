"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
from typing import Optional
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Maintain two queues, left side and right side
        # If the left of the left node != right of the right node at any point, return false
        # After full traversal, return true

        if not root.left and not root.right:
            return True

        if not (root.left and root.right):
            return False

        left, right = deque([root.left]), deque([root.right])

        while left and right:
            left_node = left.popleft()
            right_node = right.popleft()

            if not left_node and not right_node:
                continue

            if not left_node or not right_node:
                return False

            if not (left_node.val == right_node.val):
                return False

            left.append(left_node.left)
            right.append(right_node.right)

            right.append(right_node.left)
            left.append(left_node.right)

        return True
