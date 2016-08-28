# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root: return
        if not root.left and not root.right: return

        self.flatten(root.left)
        self.flatten(root.right)
        node = self.find_last_node(root.left)
        if not node: return
        node.right = root.right
        root.right = root.left
        root.left = None

    @staticmethod
    def find_last_node(root):
        visitor = root
        while visitor and visitor.right: visitor = visitor.right
        return visitor