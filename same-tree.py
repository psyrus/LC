"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false

Constraints:

The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104
"""
from collections import deque
from random import randint
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if(randint(0, 100) <= 50):
            return self.isSameTreeIterative(p, q)
        else:
            return self.isSameTreeRecursive(p, q)

    def isSameTreeRecursive(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
      if not p and not q:
          return True

      if not p or not q:
          return False

      if p.val != q.val:
          return False

      return self.isSameTreeRecursive(p.left, q.left) and self.isSameTreeRecursive(p.right, q.right)

    def isSameTreeIterative(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def checkIfNodesEqual(tree1_node: Optional[TreeNode], tree2_node: Optional[TreeNode]):
            if not tree1_node and not tree2_node:
                return True

            if not tree1_node or not tree2_node:
                return False

            return tree1_node.val == tree2_node.val

        # Need a queue for each tree
        tree1_queue = deque([p])
        tree2_queue = deque([q])

        while len(tree1_queue) > 0:
            l = tree1_queue.popleft()
            r = tree2_queue.popleft()

            if not checkIfNodesEqual(l, r): return False
            if not l: # In case both nodes were null
                continue

            # Check left side and then queue them for further checks
            if not checkIfNodesEqual(l.left, r.left): return False
            tree1_queue.append(l.left)
            tree2_queue.append(r.left)

            # Check right side and then queue them for further checks
            if not checkIfNodesEqual(l.right, r.right): return False
            tree1_queue.append(l.right)
            tree2_queue.append(r.right)

        return True


