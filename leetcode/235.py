# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        visitor = root
        while visitor:
            if visitor.val > p.val and visitor.val > q.val:
                visitor = visitor.left
            elif visitor.val < p.val and visitor.val < q.val:
                visitor = visitor.right
            else:
                return visitor