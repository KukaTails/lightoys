# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sum = 0
        self.visit(root)
        return self.sum

    def visit(self, root):
        if not root: return
        left_sub_root, right_sub_root = root.left, root.right
        if left_sub_root:
            if not left_sub_root.left and not left_sub_root.right:
                self.sum += left_sub_root.val
            else:
                self.visit(left_sub_root)
        self.visit(right_sub_root)
