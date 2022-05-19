from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def createTree(input_list: List[int]):
    tree_head = TreeNode(val=input_list[0])
    list_len = len(input_list)
    current_itr = 1
    def addNode(current_node: TreeNode):

        current_node.left = TreeNode(val=input_list[current_itr]) if current_itr < list_len - 1 else None
        current_itr += 1
        current_node.right = TreeNode(val=input_list[current_itr]) if current_itr < list_len - 1 else None
        current_itr += 1

        if current_itr < list_len - 1:
            add

    addNode(tree_head)
