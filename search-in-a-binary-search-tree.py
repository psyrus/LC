"""
You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

Example 1:
Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]

Example 2:
Input: root = [4,2,7,1,3], val = 5
Output: []
"""

# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Because a BST is guaranteed to always have left = lower value and right = higher value it can actually be done a bit like mergesort iteratively

        node = root

        while node:
            if val == node.val:
                break
            if val > node.val:
                node = node.right
            else:
                node = node.left

        return node

    def searchBSTUnoptimized(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # BST search is based on DFS I believe
        def traverse(node: TreeNode, target_val:int):
            # Break condition: If we are looking at an empty node
            # Alternative: If we are at a node that doesn't have the target value and has neither left nor right?
            if not node or node.val == target_val:
                return node

            left = traverse(node.left, target_val)
            right = traverse(node.right, target_val)

            return left or right

        return traverse(root, val)