"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        def traverse(node: TreeNode, depth):
            if not node:
                return depth - 1

            if not node.left and not node.right:
                return depth
            else:
                return max(traverse(node.left, depth + 1), traverse(node.right, depth + 1))


        return traverse(root, 1)
