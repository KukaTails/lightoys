# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        import sys
        return self.vaild(root, -sys.maxint - 1, sys.maxint)

    def vaild(self, node, low, high):
        if not node: return True
        return node.val > low and node.val < high \
               and self.vaild(node.left, low, node.val) \
               and self.vaild(node.right, node.val, high)