# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        rest = sum - root.val
        if not root.left and not root.right:
            return True if rest == 0 else False
        else:
            return self.hasPathSum(root.left, rest) or self.hasPathSum(root.right, rest)
