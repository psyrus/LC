    """

    """

    # Definition for a binary tree node.
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right


    import math
    from typing import Optional
    class Solution:
        def isValidBST(self, root: Optional[TreeNode]) -> bool:
            def confirm(node: TreeNode, max_val:int, min_val:int) -> bool:
                if not node:
                    return True

                if node.val <= min_val or node.val >= max_val:
                    return False

                return confirm(node.left, min_val=min_val, max_val=node.val) and confirm(node.right, max_val=max_val, min_val=node.val)


            return confirm(root, max_val=math.inf, min_val=(-1 * math.inf))