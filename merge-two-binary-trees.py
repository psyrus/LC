"""
You are given two binary trees root1 and root2.

Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.

Return the merged tree.

Note: The merging process must start from the root nodes of both trees.
"""

# Definition for a binary tree node.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # First instinct is to do a dfs with both tree nodes at the same time in the same direction on each recursive iteration
        # If either is null it just takes the other node

        def mergeNodes(tree1_node, tree2_node) -> TreeNode:
            if not (tree1_node and tree2_node):
                return tree1_node or tree2_node

            return TreeNode(tree1_node.val + tree2_node.val, mergeNodes(tree1_node.left, tree2_node.left), mergeNodes(tree1_node.right, tree2_node.right))

        return mergeNodes(root1, root2)
