# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        nodes = self.visit(root)
        return nodes[k - 1]
        
    def visit(self, root):
        if not root: return []
        ans = []
        if root.left:
            ans += self.visit(root.left)
        ans.append(root.val)
        if root.right:
            ans += self.visit(root.right)
        return ans