# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        import sys
        if not root: return 0
        self.result = -sys.maxsize - 1
        self.max_path_sum(root)
        return self.result

    def max_path_sum(self, root):
        if not root.left and not root.right:
            max_value = root.val
            result = max_value
        elif root.left and not root.right:
            max_value = max([root.val, root.val + self.max_path_sum(root.left)])
            result = max_value
        elif root.right and not root.left:
            max_value = max([root.val, root.val + self.max_path_sum(root.right)])
            result = max_value
        else:
            max_left_subtree = self.max_path_sum(root.left)
            max_right_subtree = self.max_path_sum(root.right)
            max_value = root.val + max([0, max_left_subtree, max_right_subtree, max_left_subtree + max_right_subtree])
            result = max([0, max_left_subtree, max_right_subtree]) + root.val
        self.result = max_value if max_value > self.result else self.result
        return result