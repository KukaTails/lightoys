# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        import sys
        min_dep = sys.maxint
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if root.left:
            min_dep = min(min_dep, self.minDepth(root.left))
        if root.right:
            min_dep = min(min_dep, self.minDepth(root.right))
        return min_dep + 1