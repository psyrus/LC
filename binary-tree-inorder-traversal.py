"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Input: root = [1,null,2,3]
Output: [1,3,2]

Input: root = []
Output: []
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Inorder means Left -> root -> right

        if not root:
            return []

        def traverse(node: TreeNode):
            if not node:
                return []

            return traverse(node.left) + [node.val] + traverse(node.right)

        return traverse(root)