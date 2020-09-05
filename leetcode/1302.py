# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    max_height = 0

    def deepestLeavesSum(self, root: TreeNode) -> int:
        self.getMaxHeight(root, 0)
        return self.getSum(root, 0)

    def getMaxHeight(self, root, height):
        if self.max_height < height:
            self.max_height = height
        if root.left != None:
            self.getMaxHeight(root.left, height + 1)
        if root.right != None:
            self.getMaxHeight(root.right, height + 1)

    def getSum(self, root, height):
        ans = 0
        if root.left == None and root.right == None and height == self.max_height:
            return root.val
        if root.left != None:
            ans += self.getSum(root.left, height + 1)
        if root.right != None:
            ans += self.getSum(root.right, height + 1)
        return ans
