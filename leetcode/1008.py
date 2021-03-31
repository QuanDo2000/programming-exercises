# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, val):
        if self.root == None:
            self.root = TreeNode(val)
            return

        curr_node = self.root
        while True:
            if val > curr_node.val:
                if curr_node.right == None:
                    curr_node.right = TreeNode(val)
                    return
                curr_node = curr_node.right
            elif val < curr_node.val:
                if curr_node.left == None:
                    curr_node.left = TreeNode(val)
                    return
                curr_node = curr_node.left


class Solution:
    def bstFromPreorder(self, preorder: list) -> TreeNode:
        tree = Tree()
        for num in preorder:
            tree.insert(num)
        return tree.root
