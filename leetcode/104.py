# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        left_depth = right_depth = 0
        if root.left is not None:
            left_depth = self.maxDepth(root.left)
        if root.right is not None:
            right_depth = self.maxDepth(root.right)
        return max(left_depth, right_depth) + 1